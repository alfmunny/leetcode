class Solution:
    def combinationSum(self, candidates, target):
        self.ans = []
        self.dfs(sorted(candidates), 0, [], target)
        return self.ans
    
    def dfs(self, candidates, index, path, target):
        if target == 0:
            self.ans.append(list(path))

        for i in range(index, len(candidates)):
            v = candidates[i]
            if v > target:
                return
            path.append(v)
            self.dfs(candidates, i, path, target-v)
            path.pop()
