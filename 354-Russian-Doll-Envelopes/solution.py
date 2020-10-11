class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0
        
        heights = [env[1] for env in sorted(envelopes, key = lambda x: [x[0], -x[1]])]
        print(heights)
        dp = [heights[0]]
        
        for i in range(1, len(heights)):
            if heights[i] > dp[-1]:
                dp.append(heights[i])
            else:
                l = self.bs(dp, heights[i])
                
                dp[l] = heights[i]
        return len(dp)

    def bs(self, dp, target):
        r = len(dp) - 1
        l = 0
        while l <= r:
            mid = (l+r) // 2
            if dp[mid] > target:
                r = mid - 1
            elif dp[mid] < target:
                l = mid + 1
                
            else:
                return mid
        return l
