class Solution:
    def superEggDrop(self, K, N):
      m = 0
      dp = [0] * (K+1)
      while dp[K] < N:
          m += 1
          prev = 0
          for i in range(1, K+1):
              tmp = dp[i]
              dp[i] = dp[i] + prev + 1
              prev = tmp
      return m
