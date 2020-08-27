class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        count = len([x for r in grid for x in r if x == 0]) + 2
        start = [[i,j] for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == 1][0]
        self.ans = 0
        self.dfs(grid, start[0], start[1], 0, count)
        return self.ans
    
    def dfs(self, grid, i, j, curCount, count):

        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] in [-1, 100]:
            return
        
        if curCount == count-1 and grid[i][j] == 2:
            self.ans += 1
            return
        elif grid[i][j] == 2:
            return
        
        x = grid[i][j]
        grid[i][j] = 100
        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            self.dfs(grid, i+di, j+dj, curCount+1, count)
            
        grid[i][j] = x
