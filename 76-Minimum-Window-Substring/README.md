# 76 - Minimum Window Substring

[leetcode](https://leetcode.com/problems/minimum-window-substring/)

## Problem

    Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).
    
    Example:
    
    Input: S = "ADOBECODEBANC", T = "ABC"
    Output: "BANC"
    Note:
    
    If there is no such window in S that covers all characters in T, return the empty string "".
    If there is such window, you are guaranteed that there will always be only one unique minimum window in S.

## Solution

```python
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target, window = defaultdict(int), defaultdict(int)
        left, right, match = 0, 0, 0
        d = float("inf")
        for c in t:
            target[c] += 1
        while right < len(s):
            c = s[right]
            if c in target:
                window[c] += 1
                if window[c] == target[c]:
                    match += 1
            right += 1

            while (match == len(target)):
                if right - left < d:
                    ans = s[left:right]
                    d = right - left

                c = s[left]
                left += 1

                if c in target:
                    if window[c] == target[c]:
                        match -= 1
                    window[c] -= 1

        return "" if d == float("inf") else ans
```
