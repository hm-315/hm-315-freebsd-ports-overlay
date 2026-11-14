--- pcapobj.cc.orig	2026-10-28 15:20:19.800980000 +0900
+++ pcapobj.cc	2026-10-28 15:20:19.801798000 +0900
@@ -334,7 +334,7 @@
   arglist = Py_BuildValue("Os#", hdr, packetdata, *len);
 #endif
 
-  result = PyEval_CallObject(pctx->pyfunc,arglist);
+  result = PyObject_CallObject(pctx->pyfunc,arglist);
 
   Py_XDECREF(arglist);
   if (result)
