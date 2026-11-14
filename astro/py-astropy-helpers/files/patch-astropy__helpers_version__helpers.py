--- astropy_helpers/version_helpers.py.orig
+++ astropy_helpers/version_helpers.py
@@ -28,7 +28,7 @@
 from distutils import log
 from configparser import ConfigParser
 
-import pkg_resources
+from packaging.version import parse as _parse_version
 
 from . import git_helpers
 from .distutils_helpers import is_distutils_display_option
@@ -58,7 +58,7 @@
     (0, 0, 0)
     """
 
-    parsed_version = pkg_resources.parse_version(version)
+    parsed_version = _parse_version(version)
 
     if hasattr(parsed_version, 'base_version'):
         # New version parsing for setuptools >= 8.0
