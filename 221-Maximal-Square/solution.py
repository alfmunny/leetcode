class Solution:
    def maximalSquare(self, matrix):
        if not matrix:
            return 0

        dp = [0 for j in range(len(matrix[0]) + 1)]
        res = 0
        prev = 0 # previous diagnol element

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                temp = dp[j+1]
                if matrix[i][j] == "1":
                    dp[j+1] = min(prev, dp[j+1], dp[j]) + 1
                    res = max(res, dp[j + 1])
                else:
                    dp[j+1] = 0
                    
                prev = dp[i+1]

        return res*res
