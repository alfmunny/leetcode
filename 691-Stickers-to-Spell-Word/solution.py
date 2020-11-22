class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        self.ret = float("inf")
        self.stickers = stickers
        self.dfs([], target, 0, 0)
        return self.ret if self.ret < float("inf") else -1
        
    def dfs(self, pool, target, index, num_s):
        if num_s >= self.ret:
            return
        if index >= len(target):
            self.ret = num_s
            return
        if target[index] in pool:
            pool.remove(target[index])
            self.dfs(pool, target, index+1, num_s)
            pool.append(target[index])
        else:
            for w in self.stickers:
                if target[index] in w:
                    new_chars = list(w)
                    new_chars.remove(target[index])
                    self.dfs(pool + new_chars, target, index+1, num_s+1)
