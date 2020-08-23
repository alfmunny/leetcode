class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        self.ans = 0
        mark = [[False] * len(grid[0]) for _ in grid]
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                self.dfs(grid, i, j, mark, 0)
                
        return self.ans
        
    def dfs(self, grid, i, j, mark, gold):
        
        if i < 0 or i == len(grid) or j < 0 or j == len(grid[0]) or mark[i][j] or not grid[i][j]:
            self.ans = max(self.ans, gold)
            return
        
        mark[i][j] = True
        
        for di, dj in [[1,0], [0, 1], [-1, 0], [0, -1]]:
            self.dfs(grid, i+di, j+dj, mark, gold+grid[i][j])

        mark[i][j] = False
