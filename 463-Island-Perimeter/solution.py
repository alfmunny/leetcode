class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    return self.dfs(grid, i, j)
        return 0

    def dfs(self, grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
            return 1

        if grid[i][j] == -1:
            return 0

        if grid[i][j]:
            grid[i][j] = -1
            return self.dfs(grid, i + 1, j) + self.dfs(
                grid, i, j + 1) + self.dfs(grid, i - 1, j) + self.dfs(
                    grid, i, j - 1)
        else:
            return 1
