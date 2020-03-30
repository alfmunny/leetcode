
# 279 - Perfect Squares

[leetcode](https://leetcode.com/problems/perfect-squares/)


## Problem

    Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.
    
    Example 1:
    
    Input: n = 12
    Output: 3 
    Explanation: 12 = 4 + 4 + 4.
    Example 2:
    
    Input: n = 13
    Output: 2
    Explanation: 13 = 4 + 9.


## Notes

DP problem

-   States: n
-   Transition:
-   dp[i] = min([_dp[i-j*j]+1 if i-j*j >= 0 else break for j in range(1, sqrt(i)+1)])

-   Base case:
    -   dp[0] = 0
    -   dp[i] = i


## Solution

    import math
    class Solution:
        dp = [0]
        def numSquares(self, n):
            _dp = self.dp
            if len(_dp) >= n + 1:
                return _dp[n]
            else:
                for i in range(len(_dp), n+1):
                    _dp += [min([_dp[i-j*j]+1 for j in range(1, int(math.sqrt(i))+1) if i-j*j >= 0])] 
            return _dp[n]
    
    print(Solution().numSquares(12))

