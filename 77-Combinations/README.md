# 77 - Combinations

[leetcode](https://leetcode.com/problems/combination-sum-ii/)

## Problem

    Share
    Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
    
    Example:
    
    Input: n = 4, k = 2
    Output:
    [
      [2,4],
      [3,4],
      [2,3],
      [1,2],
      [1,3],
      [1,4],
    ]

## Solution

```python
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        self.dfs(1, n, k, [], ans)
        return ans

    def dfs(self, index, n, k, path, ans):
        if k == 0:
            ans.append(list(path))
            return

        for i in range(index, n+1):
            path.append(i)
            self.dfs(i+1, n, k-1, path, ans)
            path.pop()

```
