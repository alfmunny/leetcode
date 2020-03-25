class Solution:
    def maxProfit(self, prices):
        max_k = 2
        dp = [ [ [0] * 2 for k in range(max_k + 1) ] for i in range(len(prices))]
        for i in range(len(prices)):
            for k in range(1, max_k + 1):
                if i == 0:
                    dp[i][k][0] = 0
                    dp[i][k][1] = -prices[i]
                else:
                    dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
                    dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])

        return dp[-1][max_k][0]

import sys
class Solution:
    def maxProfit(self, prices):
        buy = [-sys.maxsize] * 3
        sell = [0] * 3
        for price in prices:
            buy[1] = max(buy[1], sell[0]-price)
            buy[2] = max(buy[2], sell[1]-price)
            sell[1] = max(sell[1], buy[1]+price)
            sell[2] = max(sell[2], buy[2]+price)
            print(buy)
            print(sell)
        return sell[2]

print(Solution().maxProfit([3,3,5,0,0,3,1,4]))
