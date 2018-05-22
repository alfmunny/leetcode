# 238. Product of Array Except Self

Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

example:

```
Input:  [1,2,3,4]
Output: [24,12,8,6]
```

Please solve it **without division** and in O(n).


Note:

1. divide and conquer.
2. consider it in two steps.

    1. first calculate the product from left to current index. 
        [1, 2, 3, 4] -> [1, 1, 2, 6]

    2. then calculate from right to current index.
        [1, 1, 2, 6*1], multipier=1
        [1, 1, 2*4, 6], mulitplier=1*4
        [1, 1, 2*4, 6], mulitplier=1*4*3
        [1, 1*12, 2*4, 6], mulitplier=1*4*3*2
        [1*24, 1*12, 2*4, 6]
        -> [24, 12, 8, 6]
        
3. Maintain an array of the current result and a multiplier when from left to right.

