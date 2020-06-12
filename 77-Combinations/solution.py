class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        self.dfs(1, n, k, [], ans)
        return ans
    
    def dfs(self, index, n, k, path, ans):
        if k == 0:
            ans.append(list(path))
            return
        
        for i in range(index, n+1):
            path.append(i)
            self.dfs(i+1, n, k-1, path, ans)
            path.pop()
