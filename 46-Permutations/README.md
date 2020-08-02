# 46 - Permutations

[leetcode](https://leetcode.com/problems/permutations-ii/)

## Problem

    Given a collection of distinct integers, return all possible permutations.
    
    Example:
    
    Input: [1,2,3]
    Output:
    [
      [1,2,3],
      [1,3,2],
      [2,1,3],
      [2,3,1],
      [3,1,2],
      [3,2,1]
    ]

## Solution

### Solution 1

```python
class Solution:
    def permute(self, nums):
        ans = []
        self.backtrack([], nums, ans)
        return ans

    def backtrack(self, path, nums, ans):
        if not nums:
            ans.append(path[:])
            return
        for i, v in enumerate(nums):
            self.backtrack(path+[v], nums[:i]+nums[i+1:], ans)
```

### Solution 2

```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        marked = [False] * len(nums)
        self.dfs(nums, [], marked, ans)
        return ans

    def dfs(self, nums, path, marked, ans):
        if len(path) == len(nums):
            ans.append(list(path))
            return

        for i, n in enumerate(nums):
            if marked[i]:
                continue
            marked[i] = True
            path.append(n)
            self.dfs(nums, path, marked, ans)
            path.pop()
            marked[i] = False
```
