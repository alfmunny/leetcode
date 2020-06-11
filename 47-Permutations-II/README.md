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

The tricky part is how to avoid duplicates.

First sort the array.

When chose the next element, if it is the same as the previous one and the previous one is now not choosen, we should skip it, because it means the previous one has been already choosen for this position before.

    if i > 0 and nums[i] == nums[i-1] and not marked[i-1]:
      continue

```python
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        marked = [False] * len(nums)
        ans = []
        self.dfs(sorted(nums), marked, [], ans)
        return ans

    def dfs(self, nums, marked, path, ans):
        if len(path) == len(nums):
            ans.append(list(path))
            return

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1] and not marked[i-1]:
                continue
            if marked[i]:
                continue
            marked[i] = True
            path.append(nums[i])
            self.dfs(nums, marked, path, ans)
            marked[i] = False
            path.pop()
```
