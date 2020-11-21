class Solution:
    def longestPrefix(self, s: str) -> str:
        dp = [0] * len(s)
        j = 0
        i = 1
        while i < len(s):
            if s[i] == s[j]:
                j += 1
                dp[i] = j
            elif j > 0:
                j = dp[j-1]
                i -= 1
            i += 1
        return s[:dp[-1]]
