class Solution:
    def maxUncrossedLines(self, A, B):
        
        dp = [[0] * (len(A)+1) for _ in range(len(B)+1)]
        
        for i in range(len(B)):
            for j in range(len(A)):
                if B[i] == A[j]:
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1], dp[i][j] + 1)
                else:
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1], dp[i][j])
                    
        return dp[-1][-1]
