# 59 - Spiral Matrix II

[leetcode](https://leetcode.com/problems/spiral-matrix-ii/)

## Problem

    Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.
    
    Example:
    
    Input: 3
    Output:
    [
     [ 1, 2, 3 ],
     [ 8, 9, 4 ],
     [ 7, 6, 5 ]
    ]

## Solution

```python
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        step = [[0,1], [1, 0], [0, -1], [-1, 0]]
        i = j = di = 0

        for x in range(1, n * n+1):
            matrix[i][j] = x

            ni = i + step[di][0]
            nj = j + step[di][1]

            if 0 <= ni < n and 0 <= nj < n and not matrix[ni][nj]:
                i, j = ni, nj
            else:
                di = (di + 1) % 4
                i, j = i + step[di][0], j + step[di][1]

        return matrix
```
