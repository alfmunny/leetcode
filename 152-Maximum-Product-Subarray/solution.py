class Solution:
    def maxProduct(self, nums):
        rnums = nums[::-1]
        for i in range(1, len(nums)):
            nums[i] *= nums[i-1] or 1
            rnums[i] *= rnums[i-1] or 1
        return max(nums+rnums)
