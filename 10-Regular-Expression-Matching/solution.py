class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        dp = [[False] * (len(s)+1) for _ in range(len(p)+1)]
        
        dp[0][0] = True
        
        for i in range(len(p)):
            if p[i] == "*" and dp[i-1][0]:
                dp[i+1][0] = True
        
        for i in range(len(p)):
            for j in range(len(s)):
                if p[i] == s[j]:
                    dp[i+1][j+1] = dp[i][j]
                elif p[i] == '.':
                    dp[i+1][j+1] = dp[i][j]
                elif p[i] == '*':
                    if p[i-1] != s[j] and p[i-1] != '.':
                        dp[i+1][j+1] = dp[i-1][j+1]
                    else:
                        dp[i+1][j+1] = dp[i][j+1] or dp[i+1][j] or dp[i-1][j+1]                                     
        return dp[-1][-1]
