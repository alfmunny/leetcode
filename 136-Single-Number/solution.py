class Solution:
    def singleNumber(self, nums):

        res = 0

        for i in nums:
            res ^= i

        return res

print(Solution().singleNumber([2, 2, 5, 1, 8, 1, 9, 8, 9]))
