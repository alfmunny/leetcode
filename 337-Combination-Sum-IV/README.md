# 377 - Combination Sum IV

[leetcode](https://leetcode.com/problems/combination-sum-iv/submissions/)

## Problem

    Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.
    
    Example:
    
    nums = [1, 2, 3]
    target = 4
    
    The possible combination ways are:
    (1, 1, 1, 1)
    (1, 1, 2)
    (1, 2, 1)
    (1, 3)
    (2, 1, 1)
    (2, 2)
    (3, 1)
    
    Note that different sequences are counted as different combinations.
    
    Therefore the output is 7.

## Solution

It develops from DFS and then optimize it to DP problem

Consider you always choose a num as the leading number in the combination sequence.

Then for a target, the current combination would be:

    for i in nums:
      dp[target] += dp[target - i]

Note here that we should have dp[target - i] already calculdated beforehand. So we need to do it from bottom-up. And the base case would be dp[0] = 1, because when i == target, we want dp[target - i] = 1 at first, it means we find the combination.

    dp[0] = 1
    for t in range(target+1):
      for i in nums:
        dp[target] += dp[target - i]

### Solution 1: DFS

```python
class Solution:
    def combinationSum4(self, nums, target):
        self.ans = 0
        self.dfs(nums, target)
        return self.ans

    def dfs(self, nums, target):
        if target < 0:
            return

        if target == 0:
            self.ans += 1

        for i in nums:
            self.dfs(nums, target - i)
```

It exceeds time limit.

### Solution 2: DFS with memo

```python
class Solution:
    def combinationSum4(self, nums, target):
        memo = [0] * (target+1)
        self.dfs(nums, target, memo)
        return memo[target]

    def dfs(self, nums, target, memo):
        if target < 0:
            return 0

        if memo[target]:
            return memo[target]

        if target == 0:
            return 1

        ans = 0
        for i in nums:
            ans += self.dfs(nums, target - i, memo)

        memo[target] = ans

        return ans
```

It still exceeds time limit.

### Solution 3: DP

```python
class Solution:
    def combinationSum4(self, nums, target):
        dp = [0] * (target + 1) 
        dp[0] = 1

        for i in range(target+1):
            for j in nums:
                if i < j:
                    continue
                dp[i] += dp[i-j]

        return dp[-1]
```
