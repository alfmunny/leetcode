# 47 - Permutations II

[leetcode](https://leetcode.com/problems/permutations-ii/)

## Problem

    Given a collection of numbers that might contain duplicates, return all possible unique permutations.
    
    Example:
    
    Input: [1,1,2]
    Output:
    [
      [1,1,2],
      [1,2,1],
      [2,1,1]
    ]

## Solution

Backtrack problem.

Framework of backtrack problem:

1.  choose a path
2.  selection pool
3.  return condition

    ans = []
    
    def backtrack(path, pool):
    
      if meet condition:
        ans.add(path)
        return
    
      for selection in pool:
      
        path.add(selection)
        backtrack(path, new_pool)
        path.remove(selection)

**Important**:

Pay attention, you must add a copy of the path to result, not the path it self. It may get modified afterwards.

```python
class Solution:
    def permuteUnique(self, nums):
        ans = []
        self.backtrack([], nums, ans)
        return ans

    def backtrack(self, path, pool, ans):
        if not pool:
            ans.append(path[:])
            return

        t = {}

        for i, v in enumerate(pool):
            if v not in t:
                t[v] = 1
                self.backtrack(path+[v], pool[:i]+pool[i+1:], ans)

print(Solution().permuteUnique([1,1,2]))
```
