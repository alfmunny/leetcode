class Solution:
    def combinationSum4(self, nums, target):
        dp = [0] * (target + 1) 
        dp[0] = 1
        
        for i in range(target+1):
            for j in nums:
                if i < j:
                    continue
                dp[i] += dp[i-j]
                
        return dp[-1]
