class Solution:
    def findTargetSumWays(self, nums, S):
        if not nums:
            return 0
        l = len(nums)
        n = 2 * sum(nums) + 1
        offset = sum(nums)
        dp = [[0] * n for i in nums]

        dp[0][offset + nums[0]] += 1
        dp[0][offset - nums[0]] += 1

        for i in range(1, l):
            for j in range(n):
                if dp[i - 1][j] > 0:
                    if dp[i - 1][j] < n:
                        dp[i][j + nums[i]] += dp[i - 1][j]
                    if dp[i - 1][j] >= 0:
                        dp[i][j - nums[i]] += dp[i - 1][j]

        return dp[-1][offset + S]

print(Solution().findTargetSumWays([1, 1, 1, 1, 1], 3))
