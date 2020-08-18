class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        dp = [[False] * (len(s1)+1) for _ in range(len(s2)+1)]
        for i in range(len(s2)+1):
            for j in range(len(s1)+1):
                if not i and not j:
                    dp[i][j] = True
                elif not i:
                    dp[i][j] = dp[0][j-1] and s1[j-1] == s3[j-1]
                elif not j:
                    dp[i][j] = dp[i-1][0] and s2[i-1] == s3[i-1]   
                else:
                    dp[i][j] = (dp[i-1][j] and s2[i-1] == s3[i+j-1]) or (dp[i][j-1] and s1[j-1] == s3[i+j-1])
                    
        return dp[-1][-1]
