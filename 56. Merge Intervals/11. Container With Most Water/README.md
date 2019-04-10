# 11. Container With Most Water

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Input: [1,8,6,2,5,4,8,3,7]
Output: 49

Notes:
Two pointers.

1. Left pointer and right pointer
2. square = wide * min(left, right)
3. shrink the container by moving left and right pointer, if the new min(left, right) is smaller. When bigger, recalculate the new square, keep the max one.

