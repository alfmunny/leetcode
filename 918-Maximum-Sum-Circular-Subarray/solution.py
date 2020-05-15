class Solution:
    def maxSubarraySumCircular(self, A):
        curMin = 0
        curMax = 0
        minSum = sys.maxsize
        maxSum = -sys.maxsize
        s = 0
        for c in A:
            s += c
            curMax = max(c, curMax + c)
            maxSum = max(maxSum, curMax)
            curMin = min(c, curMin + c)
            minSum = min(minSum, curMin)
            
        return max(maxSum, s - minSum) if maxSum > 0 else maxSum
