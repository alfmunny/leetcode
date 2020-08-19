class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return nums
        dp = [1] * len(nums)
        pre = [i for i in range(len(nums))]
        nums.sort()
        
        max_i = 0
        
        for i in range(len(dp)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    pre[i] = j
            
                if dp[i] > dp[max_i]:
                    max_i = i
         
        ans = []
        i = max_i
        while pre[i] != i:
            ans.append(nums[i])
            i = pre[i]
        ans.append(nums[i])

        return ans
