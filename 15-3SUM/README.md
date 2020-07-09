# 15 - 3SUM

[leetcode](https://leetcode.com/problems/3sum/)

## Problem

    Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
    
    Note:
    
    The solution set must not contain duplicate triplets.
    
    Example:
    
    Given array nums = [-1, 0, 1, 2, -1, -4],
    
    A solution set is:
    [
      [-1, 0, 1],
      [-1, -1, 2]
    ]

## Solution

```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        ans = []
        nums.sort()
        for i in range(0, len(nums)-2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i-1] == nums[i]:
                continue
            left, right = i+1, len(nums)-1

            while right > left:
                s = nums[left] + nums[right] + nums[i]
                if s == 0:
                    ans.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while right > left and nums[left] == nums[left-1]:
                        left += 1
                    while right > left and nums[right] == nums[right+1]:
                        right -= 1
                elif s < 0:
                    left += 1
                else:
                    right -= 1
        return ans
```
