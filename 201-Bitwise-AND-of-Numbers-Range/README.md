# 201 - Bitwise AND of Numbers Range

[leetcode](https://leetcode.com/problems/bitwise-and-of-numbers-range/)

## Problem

    Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.
    
    Example 1:
    
    Input: [5,7]
    Output: 4
    Example 2:
    
    Input: [0,1]
    Output: 0

## Solution

m = xxx1yyyy n = xxx01zzz

`xxx` is the parts that two numbers are the same. We can definitly find these two numbers in the range

m' = xxx1000 n' = xxx0100

So the result will be xxx0000

The idea is the find position where the the numbers are the same.

```python
class Solution:
    def rangeBitwiseAnd(self, m, n):
        i = 0
        while m != n:
            m >>= 1
            n >>= 1
            i += 1
        return n << i
```
