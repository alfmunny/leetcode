class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0
        h = len(grid)
        w = len(grid[0])
        ans = 0
        m = [ [0] * w for x in range(h) ]
        for i in range(h):
            for j in range(w):
                if grid[i][j] == "1" and m[i][j] == 0:
                    self.dfs(grid, i, j, m)
                    ans += 1
        return ans
                    
    def dfs(self, grid, i, j, m):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == "0" or m[i][j] == 1:
            return None
        else:
            m[i][j] = 1
            self.dfs(grid, i, j+1, m)
            self.dfs(grid, i, j-1, m)
            self.dfs(grid, i-1, j, m)
            self.dfs(grid, i+1, j, m)
        return None
