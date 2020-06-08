class Solution:
    def rob(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        rob = nrob = rob2 = nrob2 = 0

        for n in range(1, len(nums)):
            rob, nrob = nrob + nums[n], max(rob, nrob)
            rob2, nrob2 = nrob2 + nums[n - 1], max(rob2, nrob2)

        return max(rob, nrob, rob2, nrob2)
