class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        self.dfs(1, [], ans, k, n)
        return ans
    
    
    def dfs(self, index, path, ans, k, n):
        if k == 0 and n == 0:
            ans.append(list(path))
            return
        
        for i in range(index, 10):
            if i > n:
                return
            path.append(i)
            self.dfs(i+1, path, ans, k-1, n-i)
            path.pop()
