class Solution:
    def moveZeros(self, nums):

        p1, p2 = 0, 0

        for p2 < len(nums):
            if nums[p1] != 0:
                p1 += 1
            elif nums[p2] != 0:
                nums[p1], nums[p2] = nums[p2], nums[p1]
                p1 += 1
            p2 += 1

        return nums
