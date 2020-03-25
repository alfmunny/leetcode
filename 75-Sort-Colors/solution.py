class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        lo = 0
        hi = len(nums) - 1

        while (lo < hi):
            if nums[lo] == 0:
                lo += 1
            elif nums[hi] == 2:
                hi -= 1
            elif nums[lo] == 1 and nums[hi] == 1:
                mi = lo + 1
                while (mi < hi):
                    if nums[mi] == 2 or nums[mi] == 0:
                        nums[mi], nums[hi] = nums[hi], nums[mi]
                        break
                    else:
                        mi += 1
                if mi == hi:
                    return
            else:
                nums[lo], nums[hi] = nums[hi], nums[lo]

class Solution(object):
    def sortColors(self, nums):

        lo, mi, hi = 0, 0, len(nums) - 1

        while mi <= hi: # Nottice!: here has to be <=
            if nums[mi] == 0:
                nums[mi], nums[lo] = nums[lo], nums[mi]
                lo += 1
                mi += 1
            elif nums[mi] == 2:
                nums[mi], nums[hi] = nums[hi], nums[mi]
                hi -= 1
            else:
                mi += 1
