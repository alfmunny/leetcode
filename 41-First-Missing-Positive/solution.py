class Solution(object):
    def firstMissingPositive(self, nums):
        l = len(nums)
        for i in range(l):
            # Note!: here has to be using while
            while (nums[i] > 0 and nums[i] <= l and nums[nums[i] - 1] != nums[i]):
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]

        for i, n in enumerate(nums):
            if (n != i+1):
                return i + 1

        return l + 1
