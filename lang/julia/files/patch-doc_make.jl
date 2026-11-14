--- doc/make.jl.orig	2024-08-27 21:19:31 UTC
+++ doc/make.jl
@@ -5,7 +5,30 @@ using Pkg
 empty!(DEPOT_PATH)
 pushfirst!(DEPOT_PATH, joinpath(@__DIR__, "deps"))
 using Pkg
-Pkg.instantiate()
+# Pkg.instantiate()
+Pkg.develop([
+    PackageSpec(path="deps/packages/LazilyInitializedFields"),
+    PackageSpec(path="deps/packages/RegistryInstances"),
+    PackageSpec(path="deps/packages/AbstractTrees"),
+    PackageSpec(path="deps/packages/Documenter"),
+    PackageSpec(path="deps/packages/TranscodingStreams"),
+    PackageSpec(path="deps/packages/CodecZlib"),
+    PackageSpec(path="deps/packages/DocumenterInventoryWritingBackport"),
+    PackageSpec(path="deps/packages/Preferences"),
+    PackageSpec(path="deps/packages/JLLWrappers"),
+    PackageSpec(path="deps/packages/OpenSSL_jll"),
+    PackageSpec(path="deps/packages/Libiconv_jll"),
+    PackageSpec(path="deps/packages/Git_jll"),
+    PackageSpec(path="deps/packages/Git"),
+    PackageSpec(path="deps/packages/Expat_jll"),
+    PackageSpec(path="deps/packages/ANSIColoredPrinters"),
+    PackageSpec(path="deps/packages/PrecompileTools"),
+    PackageSpec(path="deps/packages/Parsers"),
+    PackageSpec(path="deps/packages/MarkdownAST"),
+    PackageSpec(path="deps/packages/JSON"),
+    PackageSpec(path="deps/packages/IOCapture"),
+    PackageSpec(path="deps/packages/DocStringExtensions")
+])
 
 using Documenter
 using DocumenterInventoryWritingBackport
