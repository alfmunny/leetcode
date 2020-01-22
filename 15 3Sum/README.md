15. [3Sum](https://leetcode.com/problems/3sum/)

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

Notes:

1. Sort the array, consider it as a 2SUM problem with an additional loop.
2. avoid the duplicates.


Solutions:

1. Sort, 2SUM, hash table

```python
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        marker = {}
        res = []
        
        snums = sorted(nums)
        
        for i, a in enumerate(snums):
			# avoid duplicates in the outer loop
            if a not in marker:  
                hmap = {}
                l_marker = {}
                for j, b in enumerate(snums[i+1:]):
                    complement = - a - b                        
			        # avoid duplicates in the inner loop
                    if complement in hmap and b not in l_marker:
                        res.append([a, b, complement])
                        l_marker[b] = True
                    hmap[b] = True
                marker[a] = True
            else:
                continue
        
        return res
```

