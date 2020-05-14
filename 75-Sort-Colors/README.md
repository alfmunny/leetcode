# 75 - Sort Colors

[leetcode](https://leetcode.com/problems/sort-colors/)

## Problem

    Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.
    
    Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
    
    Note: You are not suppose to use the library's sort function for this problem.
    
    Example:
    
    Input: [2,0,2,1,1,0]
    Output: [0,0,1,1,2,2]
    Follow up:
    
    A rather straight forward solution is a two-pass algorithm using counting sort.
    First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
    Could you come up with a one-pass algorithm using only constant space?

## Notes

### First attempt is to use two pointer.

There is a but a corner case: when two point+begin\_src python :results output class Solution:

def subsets(self, nums): res = [[]] for i in sorted(nums): res ~~= [item~~[i] for item in res]

return res

print(Solution().subsets([1, 2, 3])) \#+end\_src

    [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

### Solution 3: backtrack

```python

class Solution(object):

    def subsets(self, nums):
        output = []
        for k in range(0, len(nums)+1):
            temp = []
            self.backtrack(0, k, nums, temp, output)

        return output

    def backtrack(self, begin, length, nums, temp, output):

        if length == len(temp):
            output.append(temp[:])

        for i in range(begin, len(nums)):
            temp.append(nums[i])
            self.backtrack(i+1, length, nums, temp, output)
            temp.pop()


print(Solution().subsets([1, 2, 3]))


```

### Solution 4: bitmask

```python

class Solution():
  def subsets(self, nums):
    n = len(nums)
    output = []
    for i in range(2**n, 2**(n+1)):
      bitmask = bin(i)[3:]
      output.append([nums[i] for i in range(n) if bitmask[i] == '1' ])

    return output
```
