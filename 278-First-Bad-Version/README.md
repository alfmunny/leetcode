# 278 - First Bad Version

[leetcode](https://leetcode.com/problems/first-bad-version/)

## Problem

    You are a product manager and currently leading a team to develop a new product. 
    Unfortunately, the latest version of your product fails the quality check. 
    Since each version is developed based on the previous version, all the versions after a bad version are also bad.
    
    Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.
    
    You are given an API bool isBadVersion(version) which will return whether version is bad. 
    Implement a function to find the first bad version. You should minimize the number of calls to the API.
    
    Example:
    
    Given n = 5, and version = 4 is the first bad version.
    
    call isBadVersion(3) -> false
    call isBadVersion(5) -> true
    call isBadVersion(4) -> true
    
    Then 4 is the first bad version. 

## Solution

Binary Search is your friend!

### Solution 1: Binary Search to the end

```python
class Solution:
    def firstBadVerion(self, n):
        l, r, mid = 1, n, (1+n) // 2

        while l != mid:
            if !isBadVersion(mid):
                l = mid
            else:
                r = mid
            mid = (l + r) // 2

        return l if isBadVersion(l) else r
```

### Solution 2: Binary Search with break

It should be faster then solution 1, because we do not wait for l meets mid, which might take longer.

```python
class Solution:
    def firstBadVersion(self, n):
        if n == 1:
            return 1

        l, r = 2, n

        while l <= r:
            mid = (l + r) // 2
            if isBadVersion(mid) and not isBadVersion(mid - 1):
                return mid
            elif isBadVersion(mid):
                r = mid - 1
            else:
                l = mid + 1
        return 1
```
