# 11. Container With Most Water

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49

Notes:

1. Two pointers.
2. How to think of it:

We have to either move the left pointer or the right pointer. We do not need to move the longer one, because the size of the container depends on the shorter one.  Thw width always descreaseMoving the longer one can not increase the square. We have to move the shorter one to find a bigger height, in order to increase the squre.

```python
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        l = 0
        r = len(height) - 1
        res = 0

        while(l < r):
            h = min(height[l], height[r])
            res = max(res, (r - l) * h)

            while(height[r] <= h and l < r):
                r -= 1
            while(height[l] <= h and l < r):
                l += 1

        return res
```
