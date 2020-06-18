class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid:
            return 0
        
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        dp = [[0] * (n+1) for _ in range(m+1)]
        
        dp[0][1] = 1
        
        for i in range(m):
            for j in range(n):
                if not obstacleGrid[i][j]:
                    dp[i+1][j+1] = dp[i+1][j] + dp[i][j+1]
                    
        return dp[-1][-1]
