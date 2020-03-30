
# 221 - Maximal Square

[leetcode](https://leetcode.com/problems/maximal-square/)


## Problem

    Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
    
    Example:
    
    Input: 
    
    1 0 1 0 0
    1 0 1 1 1
    1 1 1 1 1
    1 0 0 1 0
    
    Output: 4


## Notes

DP Problem:

-   States:
    
    -   position -> [i][j]
    -   how many continues 1 in vertical direction -> [i][j][0]
    -   how many continues 1 in horizontal direction -> [i][j][1]
    -   square value(or the length of the square) -> [i][j][2]
    
    dp[i][j][0 or 1 or 2]

-   Transition:
    
        dp[i + 1][j + 1][0] = dp[i][j + 1][0] + 1
        dp[i + 1][j + 1][1] = dp[i + 1][j][1] + 1
        dp[i + 1][j + 1][2] = min(dp[i][j][2]+1, dp[i + 1][j + 1][0], dp[i + 1][j + 1][1])

-   Base Case:
    
    One padding row on vertical and horizontal direction, with value 0


## Solution

-   **Original Version:** 

    class Solution:
        def maximalSquare(self, matrix):
            if not matrix:
                return 0
    
            dp = [[[0] * 3 for j in range(len(matrix[0]) + 1)]
                  for i in range(len(matrix) + 1)]
            res = 0
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if matrix[i][j] == "1":
                        dp[i + 1][j + 1][0] = dp[i][j + 1][0] + 1
                        dp[i + 1][j + 1][1] = dp[i + 1][j][1] + 1
                        dp[i + 1][j + 1][2] = min(dp[i][j][2]+1, dp[i + 1][j + 1][0], dp[i + 1][j + 1][1])
                        res = max(res, dp[i + 1][j + 1][2])
    
            return res*res

Time: O(mn)
Space: O(mn)

-   **Simplified Version 1: optimize the space, 3xn space:** 

    class Solution:
        def maximalSquare(self, matrix):
            if not matrix:
                return 0
    
            dp = [[0] * 3 for j in range(len(matrix[0]) + 1)]
            res = 0
    
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if matrix[i][j] == "1":
                        dp[j+1][0] = dp[j+1][0] + 1
                        dp[j+1][1] = dp[j][1] + 1
                        dp[j+1][2] = min(dp[j+1][2]+1, dp[j+1][0]+1, dp[j][1]+1)
                        res = max(res, dp[j + 1][2])
                    else:
                        dp[j+1][0] = dp[j+1][1] = dp[j+1][2] = 0
    
            return res*res

Space: O(n)

-   **Simplified Version 2: n space:** 

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

