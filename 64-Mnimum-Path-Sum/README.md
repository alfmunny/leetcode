# 64 - Minimum Path Sum

[leetcode](https://leetcode.com/problems/minimum-path-sum/)

## Problem

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

## Notes

Thinking: ~~It seems to be a greedy algorithm problem.~~

It is a dp problem.

dp equation:

dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + grid[i][j]

Remember to handle the edge cases.

## Solution

### Solution 1: 2D DP

-   Inplace DP

```python
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if i == 0:
                    if j == 0:
                        continue
                    else:
                        grid[i][j] += grid[i][j-1]
                else:
                    if j == 0:
                        grid[i][j] += grid[i-1][j]
                    else:
                        grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[-1][-1] if m and n else 0


grid = [[1,3,1],[1,5,1],[4,2,1]]

print(Solution().minPathSum(grid))
```

-   Additional DP with auxiliary columns

```python
import sys
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        dp = [[ 0 for i in range(n+1)] for j in range(m+1)]

        for i in range(len(dp)):
          dp[i][0] = sys.maxsize

        for i in range(len(dp[0])):
            dp[0][i] = sys.maxsize

        dp[1][1] = grid[0][0]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if i == 1 and j == 1: 
                    continue
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i-1][j-1]


        return dp[-1][-1] if m and n else 0


grid = [[1,3,1],[1,5,1],[4,2,1]]

print(Solution().minPathSum(grid))
```

### Solution 2: 1D DP

```python
import sys


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        dp = [sys.maxsize for i in range(n + 1)]
        dp[1] = grid[0][0]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                else:
                    dp[j + 1] = min(dp[j + 1], dp[j]) + grid[i][j]

        return dp[-1] if m and n else 0


grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]

print(Solution().minPathSum(grid))
```
