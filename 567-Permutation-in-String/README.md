# 567 - Permutation in String

[leetcode](https://leetcode.com/problems/permutation-in-string/)

## Problem

    Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.
    
     
    
    Example 1:
    
    Input: s1 = "ab" s2 = "eidbaooo"
    Output: True
    Explanation: s2 contains one permutation of s1 ("ba").
    Example 2:
    
    Input:s1= "ab" s2 = "eidboaoo"
    Output: False
     
    
    Note:
    
    The input strings only contain lower case letters.
    The length of both given strings is in range [1, 10,000].
    Accepted

## Solution

Sliding window.

```python
from collections import defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target, window = defaultdict(int), defaultdict(int)
        left, right = 0, 0
        match = 0
        for c in s1:
            target[c] += 1

        while (right < len(s2)):

            c = s2[right]
            if c in target:
                window[c] += 1
                if window[c] == target[c]:
                    match += 1

            right += 1

            while (right - left + 1 > len(s1)):
                if match == len(target):
                    return True
                c = s2[left]
                left += 1

                if c in window:
                    if window[c] == target[c]:
                        match -= 1

                    window[c] -= 1
        return False
```
