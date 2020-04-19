class Solution:
    def permuteUnique(self, nums):
        ans = []
        self.backtrack([], nums, ans)
        return ans
    
    def backtrack(self, path, pool, ans):
        if not pool:
            ans.append(path[:])
            return
        
        t = {}
        
        for i, v in enumerate(pool):
            if v not in t:
                t[v] = 1
                self.backtrack(path+[v], pool[:i]+pool[i+1:], ans)
                
print(Solution().permuteUnique([1,1,2]))
