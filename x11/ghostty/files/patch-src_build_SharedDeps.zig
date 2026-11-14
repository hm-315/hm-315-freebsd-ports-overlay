--- src/build/SharedDeps.zig.orig	2026-11-05 00:00:00 UTC
+++ src/build/SharedDeps.zig
@@ -242,7 +242,7 @@
         );
 
         if (b.systemIntegrationOption("freetype", .{})) {
-            step.root_module.linkSystemLibrary("bzip2", dynamic_link_opts);
+            step.root_module.linkSystemLibrary("bz2", dynamic_link_opts);
             step.root_module.linkSystemLibrary("freetype2", dynamic_link_opts);
         } else {
             step.root_module.linkLibrary(freetype_dep.artifact("freetype"));
