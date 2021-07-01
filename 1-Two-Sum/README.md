# [1. Two Sum](https://leetcode.com/problems/two-sum/)

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

      Because nums[0] + nums[1] = 2 + 7 = 9,
      return [0, 1].

Notes:

1. Brute force, two loops
2. Hash Table. Two Passes.

    First Pass: Make Hash Table of all elements
    Second Pass: Find the complement

```python
class Solution1(object):
  def twoSum(self, nums, target):
    h = {}
    for i, num in enumerate(nums):
      h[num] = i

    for i, num in enumerate(nums):
      complement = target - num
      if complement in h and h[complement] != i:
        return [i, h[complement]]
```

3. Hash Table. One Pass

    Find the complement in the Hash Table, save the number and its index into the Hash Table.
    The Hash Table is like a table of all complements. All numbers which do not has its complement in the table, can be the potential complement for the next ones.

```python
class Solution2(object):
    def twoSum(self, nums, target):
        h = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in h:
                h[num] = i
            else:
                return [h[n], i]
```

