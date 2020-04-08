class Solution:
    def lengthOfLIS(self, nums):
        if not nums:
            return 0
        dp = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] > dp[-1]:
                dp.append(nums[i])
            else:
                j = self.binarySearch(dp, nums[i])
                dp[j] = nums[i]

            print(dp)
        return len(dp)

    def binarySearch(self, nums, target):
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                return mid

        return l 

dp1 = [1, 5, 6, 7]
dp2 = [9, 10, 11, 12, 13]
target = 8
print(Solution().lengthOfLIS([3,5,6,2,5,4,19,5,6,7,12]))
