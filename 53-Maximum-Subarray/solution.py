class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curSum = maxSum = nums[0]

        for num in nums[1:]:
          curSum = max(num, curSum+num)
          maxSum = max(curSum, maxSum)

        return maxSum

print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 0:
            return 0

        ret = nums[0]

        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]

            ret = max(ret, nums[i])

        return ret
print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
