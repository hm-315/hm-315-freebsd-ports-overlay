--- src/algorithms/standard/nsgconstantq.cpp.orig	2026-01-01 00:00:00.000000000 +0000
+++ src/algorithms/standard/nsgconstantq.cpp	2026-01-01 00:00:00.000000000 +0000
@@ -269,6 +269,10 @@
       normalizeWeights.push_back(normalizeWeights[j]);
     }
   }
+
+  // overlay: weights are only filled for the "sine" and "impulse" modes; pad with 1 so that
+  // every window has a weight (out-of-bounds access traps with libc++ hardening).
+  normalizeWeights.resize(_freqWins.size(), 1);
 
   for (size_t j = 0; j < _freqWins.size(); j++) {
     transform(_freqWins[j].begin(), _freqWins[j].end(), _freqWins[j].begin(),
