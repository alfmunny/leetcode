class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0] * (1+len(word2)) for _ in range(1+len(word1))]
        
        for i in range(1+len(word1)):
            dp[i][0] = i
        for j in range(1+len(word2)):
            dp[0][j] = j
            
        for i in range(1, 1+len(word1)):
            for j in range(1, 1+len(word2)):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
                
        return dp[-1][-1]
