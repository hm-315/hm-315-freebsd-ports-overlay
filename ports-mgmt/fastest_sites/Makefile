# Created by: Hajime (local overlay)
# $FreeBSD$
#
# NOTE: Reconstructed local-overlay port. The original ports-mgmt/fastest_sites
# was removed from the official ports tree on 2019-10-16 (unfetchable,
# unmaintained; last version was 20110317_2, SVN r514601).
#
# This variant ships a locally maintained Python 3 port of the script
# (files/fastest_sites.py) instead of fetching the original Python 2
# distfile. The original used the `asyncore` module, which was removed in
# Python 3.12 (PEP 594); this rewrite uses select()/non-blocking sockets
# instead, so no MASTER_SITES/distinfo is needed -- the "distfile" lives
# in the port's files/ directory and is installed directly.
#
# If you'd rather keep the exact upstream Python 2 script, see the
# git history of this port for the previous USES=python:2.7 version that
# fetched fastest_sites.py from https://github.com/jordansissel/fastest_sites .

PORTNAME=	fastest_sites
PORTVERSION=	20260908
CATEGORIES=	ports-mgmt
PKGNAMESUFFIX=	-py3

MAINTAINER=	hajime.murai@gmail.com
COMMENT=	Sort MASTER_SITE_* mirrors by TCP handshake latency (local overlay, Python 3)
WWW=		https://github.com/jordansissel/fastest_sites

# Upstream never specified a license (same as the original official port).
# This Python 3 port is a local derivative work of that unlicensed script.

USES=		python:3.6+ shebangfix
SHEBANG_FILES=	${WRKSRC}/fastest_sites.py

NO_ARCH=	yes
NO_BUILD=	yes

# No MASTER_SITES/DISTFILES: the source lives in files/ below, not fetched.
DISTFILES=

PLIST_FILES=	bin/fastest_sites

do-extract:
	@${MKDIR} ${WRKSRC}
	@${CP} ${FILESDIR}/fastest_sites.py ${WRKSRC}/

do-install:
	${INSTALL_SCRIPT} ${WRKSRC}/fastest_sites.py ${STAGEDIR}${PREFIX}/bin/fastest_sites

.include <bsd.port.mk>
