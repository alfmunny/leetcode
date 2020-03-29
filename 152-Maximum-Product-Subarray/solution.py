class Solution:
    def maxProduct(self, nums):
        if not nums:
            return 0
        
        pos = neg = res = nums[0]
        for i in nums[1:]:
            if i>=0:
                pos, neg = max(i, pos*i), neg*i
            else:
                pos, neg = neg*i, min(i, pos*i)
            res = max(pos, res)
        return res
