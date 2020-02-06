# [34. Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Notes:

here are some sub problems to think about.

1. How to find the left most one in a sorted array

```python
  def findLeftmost(self, nums, target):
    if len(nums) == 0:
      return -1

    l, r = 0, len(nums) - 1
    while l < r:
      # default biased to the left one
      mid = (l + r) // 2

      # always move the left one if target is in the right part
      if target > nums[mid]:
        l = mid + 1
      else:
        r = mid

    return l if nums[l] == target else -1
```

2. How to find the right most one in a sorted array

```python
  def findRightmost(self, nums, target):

    if len(nums) == 0:
      return -1

    l, r = 0, len(nums) - 1

    while l < r:
      # biased to the right one
      mid = (l + r) // 2 + 1

      # always move the right one if target is in the left part
      if target < nums[mid]:
        r = mid - 1
      else:
        l = mid

    return l if nums[l] == target else -1

```

3. Whole solution
```python
  def searchRange(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    l, r = 0, len(nums) - 1
    res = [-1, -1]

    if len(nums) == 0:
      return res

    # find the leftmost one
    while (l < r):
      mid = (l + r) // 2

      # always move left pointer if target is not found
      if nums[mid] < target:
        l = mid + 1
      else: # always move the right pointer if the target is found or in the right part
        r = mid

    # No target found
    if nums[l] != target:
      return res

    res[0] = l


    # find the rightmost one
    # l is already the leftmost one,
    # we only have to reset the right pointer
    r = len(nums) - 1

    while l < r:
      # biased on the right
      mid = (l + r) // 2 + 1

      if nums[mid] > target:
        r = mid - 1
      else:
        l = mid


    res[1] = l
    return res
```


