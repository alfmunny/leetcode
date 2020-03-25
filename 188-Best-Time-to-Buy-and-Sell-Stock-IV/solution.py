class Solution:
    def maxProfit(self, k, prices):
        if not prices:
            return 0

        n = len(prices)
        if k >= n//2: # treat it as infinitive transactions
            res = 0
            for i in range(1, n):
                if prices[i] > prices[i-1]:
                    res += prices[i] - prices[i-1]
            return res

        buy = [-sys.maxsize] * (k+1)
        sell = [0] * (k+1)

        for price in prices:
            for i in range(1, k+1):
                buy[i] = max(buy[i], sell[i-1]-price)
                sell[i] = max(sell[i], buy[i]+price)


        return sell[-1]
