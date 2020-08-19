class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        self.ans = 0
        mark = [False] * len(tiles)
        self.dfs(sorted(tiles), mark)
        return self.ans
    
    def dfs(self, tiles, mark):
        for i in range(len(tiles)):
            if mark[i] or (i > 0 and tiles[i] == tiles[i-1] and not mark[i-1]):
                continue
            mark[i] = True
            self.ans += 1
            self.dfs(tiles, mark)
            mark[i] = False
