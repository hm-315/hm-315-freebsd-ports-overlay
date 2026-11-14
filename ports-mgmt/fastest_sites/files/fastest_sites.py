#!/usr/bin/env python3
#
# Author: Jordan Sissel (original Python 2 version)
# Python 3 port: local overlay maintenance
#
# This script will run through all entries for MASTER_SITE_* variables in
# bsd.sites.mk and emit the list of sites in order of who is probably fastest
# for your location.
#
# The ordering is determined by the latency of connecting to the specific site.
#
# Usage: fastest_sites.py [varname varname2 .. varnameN]
#
# 'varname' is one of the MASTER_SITE_FOO variables from bsd.sites.mk.
# If no varnames are specified, all MASTER_SITE_* variables are tested.
# Otherwise, only the varnames given will be tested.
#
# The output is suitable for Makefiles, or make.conf. However, I recommend:
#
# in make.conf:
#   .include "/usr/local/etc/ports_sites.conf"
#
# and use:
#   ./fastest_sites.py > /usr/local/etc/ports_sites.conf
#
# Doing so this way will allow you to regenerate ports_sites.conf on a whim
# without having to worry about obliterating anything in /etc/make.conf
#
# --- Notes on this Python 3 port ---
# The original implementation used the `asyncore` module, which was
# deprecated in Python 3.6 and removed entirely in Python 3.12 (PEP 594).
# This port replaces it with a small non-blocking-socket + select() based
# event loop that reproduces the same behavior: open many TCP connections
# in parallel, measure how long each takes to complete the handshake, and
# use that as a proxy for latency/distance to the mirror.

import os
import re
import select
import socket
import subprocess
import sys
import time
from urllib.parse import urlsplit

socket.setdefaulttimeout(5)

SCHEME_PORTS = {
    "http": 80,
    "ftp": 21,
    "https": 443,
}


class PendingConnect:
    """Tracks a single in-progress non-blocking TCP connect."""

    def __init__(self, url):
        self.url = url
        self.start_time = time.time()
        self.sock = None
        self.done = False

        try:
            self.host, self.port = self._parse_url(url)
        except (ValueError, KeyError):
            self.done = True
            return

        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.setblocking(False)
            # For a non-blocking socket, connect() raises BlockingIOError
            # (EINPROGRESS) immediately; that's expected, not an error.
            try:
                self.sock.connect((self.host, self.port))
            except BlockingIOError:
                pass
            except OSError:
                self.done = True
        except socket.gaierror:
            self.done = True

    @staticmethod
    def _parse_url(url):
        parts = urlsplit(url)
        scheme = parts.scheme.lower()
        if not parts.hostname:
            raise ValueError("no hostname in %r" % (url,))
        return parts.hostname, SCHEME_PORTS[scheme]

    def close(self):
        if self.sock is not None:
            try:
                self.sock.close()
            except OSError:
                pass
        self.done = True


def GetVariable(varname):
    if varname in os.environ:
        return os.environ[varname]
    make = "make -f /usr/ports/Makefile -V %s" % varname
    value = Run(make)
    if value.endswith("\n"):
        value = value[:-1]
    return value


def Run(cmd):
    proc = subprocess.run(
        ["/bin/sh", "-c", cmd], stdout=subprocess.PIPE, text=True
    )
    return proc.stdout


def FindFastest(varname, sitelist):
    latencies = {}

    # Ignore duplicates
    sitelist = set(sitelist)

    pending = [PendingConnect(url) for url in sitelist]
    # Sockets that failed to even start (bad host, DNS error, etc.) count
    # as "very slow" so they sort to the bottom, matching the original
    # behavior of callback(url, 1000).
    for p in pending:
        if p.done:
            latencies[p.url] = 1000

    live = [p for p in pending if not p.done]

    # We probably don't need more than 10 results, so if there are more
    # than 10 servers, let's only wait for the first few that return
    # quickly. This target is measured against the whole batch (including
    # sites that already failed synchronously above), not just the ones
    # still connecting, so we don't stop early just because a couple of
    # bad hosts padded out the latencies dict.
    target_count = min(len(pending), 10)

    _run_select_loop(live, latencies, overall_timeout=1, target_count=target_count)

    if not latencies:
        # No data has come back yet, let's wait longer.
        print(" => Still waiting on data for %s" % varname, file=sys.stderr)
        _run_select_loop(live, latencies, overall_timeout=30, target_count=None)

    # Close any still-open connections...
    for p in live:
        if not p.done:
            p.close()

    # Return the latency dict sorted by latency as list of (key, value)
    latency_list = sorted(latencies.items(), key=lambda item: (item[1], item[0]))
    return latency_list


def _run_select_loop(pending, latencies, overall_timeout, target_count):
    """Poll `pending` PendingConnect objects with select() until they
    finish connecting (or error out), recording durations into
    `latencies`, similar to asyncore.loop(timeout=..., count=...).
    """
    deadline = time.time() + overall_timeout
    while True:
        live = [p for p in pending if not p.done and p.sock is not None]
        if not live:
            return
        if target_count is not None and len(latencies) >= target_count:
            return

        remaining = deadline - time.time()
        if remaining <= 0:
            return

        wlist = [p.sock for p in live]
        xlist = [p.sock for p in live]
        try:
            _, writable, exceptional = select.select([], wlist, xlist, remaining)
        except (OSError, ValueError):
            return

        by_sock = {p.sock: p for p in live}

        for sock in exceptional:
            p = by_sock.get(sock)
            if p is None:
                continue
            p.close()

        for sock in writable:
            p = by_sock.get(sock)
            if p is None:
                continue
            # Writable on a connecting non-blocking socket means the
            # connect attempt has finished; check SO_ERROR to see if it
            # actually succeeded.
            err = p.sock.getsockopt(socket.SOL_SOCKET, socket.SO_ERROR)
            duration = time.time() - p.start_time
            if err == 0:
                latencies.setdefault(p.url, 0)
                latencies[p.url] += duration
            else:
                latencies[p.url] = 1000
            p.close()


var_re = re.compile(r"^(MASTER_SITE_[A-Z_]+)\+?=")
sites_mk = "%s/Mk/bsd.sites.mk" % (GetVariable("PORTSDIR"))
sites = {}
bad_sites = {}

# Some sites use variables in them and due to the way we request the list of
# sites these variables are not set, resulting in useless urls like
# "http://.googlecode.com/files" because the original value was set to
# "http://${PORTNAME}.googlecode.com/files"
# We don't have access to those variables so we skip them.
# It also catches http://www..com just in case that pops up in the future
bad_site_regex = re.compile(r"(\/\/\.|\.\.|[a-zA-Z]\/\/)")

with open(sites_mk, "r") as fd:
    for line in fd:
        match = var_re.search(line)
        if match:
            varname = match.group(1)
            output = Run("make -V %s -f %s" % (varname, sites_mk))

            if bad_site_regex.search(output):
                bad_sites[varname] = output.split()
            else:
                sites[varname] = output.split()

for varname, sitelist in sites.items():
    if len(sys.argv) > 1 and varname not in sys.argv[1:]:
        continue

    print(
        " => Checking servers for %s (%d servers)" % (varname, len(sitelist)),
        file=sys.stderr,
    )
    latency_list = FindFastest(varname, sitelist)

    # Don't print the trailing slash on the last line.
    print("%s=\\" % varname)
    print(" \\\n".join(url for url, duration in latency_list))

    print()
    sys.stdout.flush()

# Walk the dict of bad sites that we know cause problems.
# If explicitly asked to sort one of them be verbose about skipping it
# otherwise be silent.
for varname, sitelist in bad_sites.items():
    if len(sys.argv) > 1 and varname in sys.argv[1:]:
        print("Unable to sort %s - skipping." % varname, file=sys.stderr)
