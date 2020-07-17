# 461 - Hamming Distance

[leetcode](https://leetcode.com/problems/hamming-distance/)

## Problem

    The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
    
    Given two integers x and y, calculate the Hamming distance.
    
    Note:
    0 ≤ x, y < 231.
    
    Example:
    
    Input: x = 1, y = 4
    
    Output: 2
    
    Explanation:
    1   (0 0 0 1)
    4   (0 1 0 0)
           ↑   ↑
    
    The above arrows point to positions where the corresponding bits are different.
    Accepted

## Solution

### Solution 1:

```python
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        z = x ^ y
        s = 0
        while z:
            s += z & 1
            z = z >> 1
        return s
```

### Solution 2: t & (t - 1)

```python
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        z = x ^ y
        s = 0
        while z:

            s += 1
            z = z & (z - 1)

        return s
```
