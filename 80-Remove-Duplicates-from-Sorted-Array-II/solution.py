class Solution:
    def removeDuplicates(self, nums):
        i = 0
        k = 2
        for n in nums:
            if i < k or n > nums[i-k]:
                nums[i] = n
                i += 1
        return i
