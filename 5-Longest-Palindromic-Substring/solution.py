class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[0] * len(s) for i in range(len(s))]
        res = ""
        for r in range(len(s)):
            for l in range(r + 1):
                if s[l] == s[r]:
                    if l == r or l + 1 == r or dp[l + 1][r - 1] == 1:
                        dp[l][r] = 1
                        if r - l + 1 > len(res):
                            res = s[l:r + 1]
        return res
