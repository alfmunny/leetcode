# 64. Minimum Path Sum

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]

Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.


Notes:

DP problem.

    x[i][j] = min(x[i-1][j], x[i][j-1]) +  grid[i][j]

Remember to initialize the first row and the first column for the DP memory x
