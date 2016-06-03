# [3Sum Closest](https://leetcode.com/problems/3sum-closest/)

Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. 
You may assume that each input would have exactly one solution.

```
For example, given array S = {-1 2 1 -4}, and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
```
## Notes:

1. Sort the array first.
2. Use two pointers, one at head, one at tail. Solve it like a 2Sum problem, only you have to loop it for every element in the array. 
3. The complexity of 2Sum problem is O(NlogN)(Because quicksort has O(NlogN) and the find process takes only linear time N by using two pointers.)
So the complexity of 3Sum problem is O(N^2 + NlogN) = O(N^2).