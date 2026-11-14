Reject control characters in POP3 commands (CVE-2025-15367, gh-143923).

Upstream commit b234a2b (python/cpython#143924) only landed on main (3.15);
it was not backported to 3.14. Applied here as a local security patch.
Note: user names and passwords containing C0 control characters
(0x00-0x1F, 0x7F) are now rejected with ValueError.

--- Lib/poplib.py.orig
+++ Lib/poplib.py
@@ -121,6 +121,8 @@
 
     def _putcmd(self, line):
         if self._debugging: print('*cmd*', repr(line))
         line = bytes(line, self.encoding)
+        if re.search(b'[\x00-\x1F\x7F]', line):
+            raise ValueError('Control characters not allowed in commands')
         self._putline(line)
 
