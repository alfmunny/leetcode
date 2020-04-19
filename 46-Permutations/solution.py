class Solution:
    def permute(self, nums):
        ans = []
        self.backtrack([], nums, ans)
        return ans
        
    def backtrack(self, path, nums, ans):
        if not nums:
            ans.append(path[:])
            return
        for i, v in enumerate(nums):
            self.backtrack(path+[v], nums[:i]+nums[i+1:], ans)
