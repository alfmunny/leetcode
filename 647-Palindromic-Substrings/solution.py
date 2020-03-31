class Solution:
    def countSubstrings(self, s):
        dp = [[0] * len(s) for i in range(len(s))]
        res = 0
        for r in range(len(s)):
            for l in range(r+1):
                if s[r] == s[l]:
                    if r == l or r+1 == l or dp[l+1][r-1] == 1:
                        dp[l][r] = 1
                        res += 1
        return res
print(Solution().countSubstrings("aba"))
