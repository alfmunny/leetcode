class Solution:
    def findDisappearedNumbers(self, nums):
        for i in nums:
            j = i
            while nums[j-1] != j:
                nums[j-1], j = j, nums[j-1]

        return [i+1 for i in range(len(nums)) if nums[i] != i+1]
