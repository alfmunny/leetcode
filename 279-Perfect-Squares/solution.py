class Solution:
    dp = [0]
    def numSquares(self, n):
        _dp = self.dp
        if len(_dp) >= n + 1:
            return _dp[n]
        else:
            for i in range(len(_dp), n+1):
                _dp += [i]
                j = 1
                while i - j*j >= 0:
                    _dp[i] = min(_dp[i-j*j]+1, _dp[i])
                    j += 1  
        return _dp[n]
