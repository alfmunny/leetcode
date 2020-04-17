# 238 - Product of Array Except Self

[leetcode](https://leetcode.com/problems/product-of-array-except-self/)

## Problem

    238. Product of Array Except Self
    Medium
    
    4145
    
    358
    
    Add to List
    
    Share
    Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
    
    Example:
    
    Input:  [1,2,3,4]
    Output: [24,12,8,6]
    Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.
    
    Note: Please solve it without division and in O(n).
    
    Follow up:
    Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)

## Solution

### Solution 1: prefix product and suffix product

```python
class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        ans = [0] * n
        ans[0] = 1

        for i in range(1, n):
            ans[i] = ans[i-1] * nums[i-1]

        R = 1
        for i in reversed(range(n)):
            ans[i] = ans[i] * R
            R *= nums[i]

        return ans

print(Solution().productExceptSelf([1, 2, 3, 4]))
```
