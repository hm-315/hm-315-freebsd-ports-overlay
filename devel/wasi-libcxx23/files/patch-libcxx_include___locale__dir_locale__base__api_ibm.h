libc++ 23 has no WASI branch in locale_base_api.h and falls back to ibm.h,
whose strtod_l/strtof_l/strtold_l/vasprintf conflict with the declarations
already provided by wasi-libc (wasi-sdk 34) in stdlib.h/stdio.h.

--- libcxx/include/__locale_dir/locale_base_api/ibm.h.orig
+++ libcxx/include/__locale_dir/locale_base_api/ibm.h
@@ -53,6 +53,7 @@
 
 // The following are not POSIX routines.  These are quick-and-dirty hacks
 // to make things pretend to work
+#if !defined(__wasi__)
 inline _LIBCPP_HIDE_FROM_ABI double strtod_l(const char* __nptr, char** __endptr, locale_t locale) {
   __setAndRestore __newloc(locale);
   return ::strtod(__nptr, __endptr);
@@ -94,4 +95,6 @@
   return str_size;
 }
 
+#endif // !defined(__wasi__)
+
 #endif // _LIBCPP___LOCALE_DIR_LOCALE_BASE_API_IBM_H
