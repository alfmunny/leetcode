# 368 - Largest Divisible Subset

[leetcode](https://leetcode.com/problems/largest-divisible-subset/)

## Problem

    Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies:
    
    Si % Sj = 0 or Sj % Si = 0.
    
    If there are multiple solutions, return any subset is fine.
    
    Example 1:
    
    Input: [1,2,3]
    Output: [1,2] (of course, [1,3] will also be ok)
    
    Example 2:
    
    Input: [1,2,4,8]
    Output: [1,2,4,8]

## Solution

### Solution 1: DP

```python
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return nums
        dp = [1] * len(nums)
        pre = [i for i in range(len(nums))]
        nums.sort()

        max_i = 0

        for i in range(len(dp)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    pre[i] = j

                if dp[i] > dp[max_i]:
                    max_i = i

        ans = []
        i = max_i
        while pre[i] != i:
            ans.append(nums[i])
            i = pre[i]
        ans.append(nums[i])

        return ans
```

### Solution 2: Hash

1.  Sort the numbers
2.  Store the answers for every number while go through the numbers

```python
class Solution:
    def largestDivisibleSubset(self, nums):
        S = {-1: set()}
        H = {}
        for n in sorted(nums):
            H[n] = max((H[d] for d in S if x % d == 0), key=len) | {n}
        return list(max(S.values(), key=len))
```
