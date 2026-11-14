Obtained from:  https://github.com/RDFLib/html5rdf/commit/3b49bab9e4ca79e54d37f47711f558b525eb2db3
		https://github.com/RDFLib/html5rdf/commit/eb0fbab7ba6b7b855c150c3fe42633d860f629c1

Additionally: guard the pkg_resources import. setuptools >= 82 dropped
pkg_resources entirely, and the code guarded by "if pkg_resources:" below
is dead anyway on any setuptools newer than 18.5 (2015) -- it only exists
to work around markerlib bugs in ancient setuptools. Making the import
optional lets setup.py run unchanged on modern setuptools where
pkg_resources simply doesn't exist.

--- setup.py.orig	2024-10-23 11:21:43 UTC
+++ setup.py
@@ -5,9 +5,11 @@

 from os.path import join, dirname
 from setuptools import setup, find_packages, __version__ as setuptools_version
-from pkg_resources import parse_version
-
-import pkg_resources
+try:
+    import pkg_resources
+    from pkg_resources import parse_version
+except ImportError:
+    pkg_resources = None

 try:
     import _markerlib.markers
@@ -87,8 +89,8 @@ with open(join(here, "html5rdf", "__init__.py"), "rb")
         if (len(a.targets) == 1 and
                 isinstance(a.targets[0], ast.Name) and
                 a.targets[0].id == "__version__" and
-                isinstance(a.value, ast.Str)):
-            version = a.value.s
+                isinstance(a.value, ast.Constant)):
+            version = a.value.value

 setup(name='html5rdf',
       version=version,
