class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        
        first_diff = 1
        dp = [1] * len(nums)
        ret = 1
        
        for first_diff in [1, -1]:
            dp = [1] * len(nums)
            for i in range(1, len(nums)):
                if first_diff * (nums[i] - nums[i-1]) > 0:
                    dp[i] = dp[i-1] + 1
                    first_diff *= -1
                else:
                    dp[i] = dp[i-1]
                    
            ret = max(ret, max(dp))
            
        return ret
