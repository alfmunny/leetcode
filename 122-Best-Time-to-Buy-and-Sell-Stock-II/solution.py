class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0

        valley = prices[0]
        maxProfit = 0
        res = 0

        for price in prices:
            if price - valley < maxProfit:
                valley = price # new valley
                res += maxProfit # add the current maxProfit
                maxProfit = 0 # reset current maxProfit
            else:
                maxProfit = price - valley # update the maxProfit when we still go up

        # remember to add the last maxProfit.
        # 1. When we are on the peak. maxProfit > 0, it should be added
        # 2. When we are in the vally, maxProfit = 0, would not affect the value
        res += maxProfit

        return res

class Solution:
    def maxProfit(self, prices):
        res = 0
        for i in range(1, len(prices)):
            if (prices[i-1] < prices[i]):
                res += prices[i] - prices[i-1]
        return res
