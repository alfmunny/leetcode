import sys
class Solution:
    def maxProfit(self, prices):
        dp_buy = -sys.maxsize
        dp_sell = 0
        dp_pre_0 = 0

        for price in prices:
            tmp = dp_sell
            dp_sell = max(dp_sell, dp_buy + price)
            dp_buy = max(dp_buy, dp_pre_0 - price)
            dp_pre_0 = tmp

        return dp_sell
