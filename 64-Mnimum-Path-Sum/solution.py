import sys
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        dp = [[ 0 for i in range(n+1)] for j in range(m+1)]

        for i in range(len(dp)):
          dp[i][0] = sys.maxsize

        for i in range(len(dp[0])):
            dp[0][i] = sys.maxsize

        dp[1][1] = grid[0][0]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if i == 1 and j == 1: 
                    continue
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i-1][j-1]


        return dp[-1][-1] if m and n else 0


grid = [[1,3,1],[1,5,1],[4,2,1]]

print(Solution().minPathSum(grid))
