dp[i][j] = dp[i-1][j] + dp[i][j-1]

dp[j] = dp[j - 1] + dp[j]

class Solution():
    def uniquePath(self, m, n):
        dp = [[1 for j in range(n)] for i in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

        return dp[-1][-1] if m and n else 0

class Solution():
    def uniquePath(self, m, n):
        dp = [1] * n

        for i in range(1, m):
            for j in range(1, n):
                dp[j] = dp[j - 1] + dp[j]

        return dp[-1] if m and n else 0
