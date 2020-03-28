class Solution:
    def rob(self, nums):
        robbed, notRobbed = 0, 0
        for i in nums:
            robbed, notRobbed = notRobbed + i, max(robbed, notRobbed)
        return max(robbed, notRobbed)
