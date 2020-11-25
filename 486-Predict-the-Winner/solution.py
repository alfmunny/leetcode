class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        dp = {}
        def getMaxDiff(left, right):
            if (left, right) not in dp:
                if left == right:
                    return nums[left]
                
                dp[left, right] = max(nums[left] - getMaxDiff(left+1, right), nums[right] - getMaxDiff(left, right-1))
            return dp[left, right]
                
        return getMaxDiff(0, len(nums)-1) >= 0
