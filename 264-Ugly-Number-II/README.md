# 264 - Ugly Number II

[leetcode](https://leetcode.com/problems/ugly-number-ii/)

## Problem

    Write a program to find the n-th ugly number.
    
    Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 
    
    Example:
    
    Input: n = 10
    Output: 12
    Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
    Note:  
    
    1 is typically treated as an ugly number.
    n does not exceed 1690.

## Solution

```python
class Solution:
    ugly = sorted(2**a * 3**b * 5**c for a in range(32) for b in range(32) for c in range(32))
    def nthUglyNumber(self, n: int) -> int:
        return self.ugly[n-1]
```
