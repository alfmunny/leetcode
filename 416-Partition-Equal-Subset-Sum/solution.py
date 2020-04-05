class Solution:
    def canPartition(self, nums):
        s = sum(nums)
        if s%2 != 0:
            return False

        bits = 1
        for i in nums:
            bits |= bits << i

        return (bits >> (s//2)) & 1 == 1
