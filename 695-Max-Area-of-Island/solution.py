class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        if not grid or not grid[0]:
            return 0
        
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > 0:
                    ans = max(ans, self.dfs(grid, i, j))
        return ans
    
    def dfs(self, grid, i, j):
        
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or not grid[i][j]:
            return 0
            
        grid[i][j] = 0
        count = 1
        count += self.dfs(grid, i+1, j)
        count += self.dfs(grid, i-1, j)
        count += self.dfs(grid, i, j+1)
        count += self.dfs(grid, i, j-1)
        return count
