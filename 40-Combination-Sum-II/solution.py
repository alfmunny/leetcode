class Solution:
    def combinationSum(self, candidates, target):
        self.ans = []
        candidates.sort()
        self.dfs(candidates, 0, [], target)
        return self.ans

    def dfs(self, candidates, index, path, target):
        if target < 0:
            return

        if target == 0:
            self.ans.append(list(path))

        for i in range(index, len(candidates)):
            if i > index and candidates[i] == candidates[i-1]:
                continue
            path.append(candidates[i])
            self.dfs(i+1, candidates, path, target-candidates[i])
            path.pop()
