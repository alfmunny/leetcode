class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        marked = [False] * len(nums)
        ans = []
        self.dfs(sorted(nums), marked, [], ans)
        return ans
    
    def dfs(self, nums, marked, path, ans):
        if len(path) == len(nums):
            ans.append(list(path))
            return
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1] and not marked[i-1]:
                continue
            if marked[i]:
                continue
            marked[i] = True
            path.append(nums[i])
            self.dfs(nums, marked, path, ans)
            marked[i] = False
            path.pop()
