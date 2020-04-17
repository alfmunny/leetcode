# 678 - Valid Parenthesis String

[leetcode](https://leetcode.com/problems/valid-parenthesis-string/)

## Problem

    Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:
    
    Any left parenthesis '(' must have a corresponding right parenthesis ')'.
    Any right parenthesis ')' must have a corresponding left parenthesis '('.
    Left parenthesis '(' must go before the corresponding right parenthesis ')'.
    '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
    An empty string is also valid.
    Example 1:
    Input: "()"
    Output: True
    Example 2:
    Input: "(*)"
    Output: True
    Example 3:
    Input: "(*))"
    Output: True
    Note:
    The string size will be in the range [1, 100].

## Solution

### Solution 1: cmin and cmax to valida to parenthesis

```python
class Solution:
    def checkValidString(self, s: str) -> bool:
        counter_max = 0
        counter_min = 0

        for c in s:
            if c == "(":
                counter_max += 1
                counter_min += 1
            elif c == ")":
                counter_max -= 1
                counter_min = max(counter_min-1, 0)
            else:
                counter_max += 1
                counter_min = max(counter_min-1, 0)

            if counter_max < 0:
                return False

        return counter_min == 0
```
