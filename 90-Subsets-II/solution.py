class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        marked = [False] * len(nums)
        
        self.dfs(sorted(nums), 0, [], ans, marked)
        
        return ans
    
    def dfs(self, nums, index, path, ans, marked):
        ans.append(list(path))
        for i in range(index, len(nums)):
            if i > 0 and nums[i] == nums[i-1] and not marked[i-1]:
                continue
            
            marked[i] = True
            path.append(nums[i])
            self.dfs(nums, i+1, path, ans, marked)
            path.pop()
            marked[i] = False
