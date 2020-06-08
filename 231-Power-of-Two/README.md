# 231 - Power of Two

[leetcode](https://leetcode.com/problems/power-of-two/)

## Problem

    Given an integer, write a function to determine if it is a power of two.
    
    Example 1:
    
    Input: 1
    Output: true 
    Explanation: 20 = 1
    
    Example 2:
    
    Input: 16
    Output: true
    Explanation: 24 = 16
    
    Example 3:
    
    Input: 218
    Output: false

## Solution

### Solution 1: Straight forward

```python
class Solution:
    def powerOfTwo(self, n):
        while n != 1:
            if n % 2:
                return False
            n //= 2

        return True
```

### Solution 2: Bit manipulation

power of two: n = 1000000 n - 1 = 111111 n & (n-1) == 0

Note: n can not be 0

```python
class Solution:
    def powerOfTwo(self, n):
        return n and not (n & n-1)
```
