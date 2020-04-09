# 844 - Backspace String Compare

[leetcode](https://leetcode.com/problems/backspace-string-compare/)

## Problem

    Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.
    
    Example 1:
    
    Input: S = "ab#c", T = "ad#c"
    Output: true
    Explanation: Both S and T become "ac".
    Example 2:
    
    Input: S = "ab##", T = "c#d#"
    Output: true
    Explanation: Both S and T become "".
    Example 3:
    
    Input: S = "a##c", T = "#a#c"
    Output: true
    Explanation: Both S and T become "c".
    Example 4:
    
    Input: S = "a#c", T = "b"
    Output: false
    Explanation: S becomes "c" while T becomes "b".
    Note:
    
    1 <= S.length <= 200
    1 <= T.length <= 200
    S and T only contain lowercase letters and '#' characters.

## Solution

### Solution 1: stack

```python
class Solution:
    def backspaceCompare(self, S, T):
        return self.build(S) == self.build(T)

    def build(self, s):
        res = []

        for c in s:
            if c != "#":
                res.append(c)
            elif res:
                res.pop()

        return "".join(res)

print(Solution().backspaceCompare("ac#cc#", "ab#c"))
```

```python
from functools import reduce

class Solution:
    def backspaceCompare(self, S, T):
        def back(res, c):
            if c != "#":
                res.append(c)
            elif res:
                res.pop()
            return res

        return reduce(back, S, []) == reduce(back, T, [])

print(Solution().backspaceCompare("ac#cc#", "ab#c"))
```

### Solution 2: two pointer, reserve

```python
class Solution:
    def backspaceCompare(self, S, T):
        pS, pT = len(S) - 1, len(T) - 1
        backS, backT = 0, 0

        while pS >= 0 or pT >= 0:
            while pS >= 0:
                if S[pS] == "#":
                    backS += 1
                    pS -= 1
                elif backS:
                    backS -= 1
                    pS -= 1
                else:
                    break

            while pT >= 0:
                if T[pT] == "#":
                    backT += 1
                    pT -= 1
                elif backT:
                    backT -= 1
                    pT -= 1
                else:
                    break

            if not (pS >= 0 and pT >= 0 and S[pS] == T[pT]):
                return pS == pT == -1

            pS -= 1
            pT -= 1

        return True
print(Solution().backspaceCompare("###ac#b", "ab#b"))
```
