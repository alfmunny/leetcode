# 17 - Letter Combinations of a Phone Number

[leetcode](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)

## Problem

    Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
    
    A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
    
    Example:
    Input: "23"
    Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

## Solution

#### Solution 1: DFS

```python
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        m = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }
        ans = []
        self.dfs(0, digits, m, [], ans)

        return ans

    def dfs(self, index, digits, m, path, ans):
        if not digits:
            return
        if index == len(digits):
            ans.append("".join(path))
            return
        for c in m[int(digits[index])]:
            path.append(c)
            self.dfs(index+1, digits, m, path, ans)
            path.pop()
```

#### Solution 2: iterative

```python
class Solution:
    def letterCombination(self, digits):
          m = {
              2: "abc",
              3: "def",
              4: "ghi",
              5: "jkl",
              6: "mno",
              7: "pqrs",
              8: "tuv",
              9: "wxyz"
          }

        ans = [""]

        for d in digits:
            ans = [ ans[i] + c for c in m[int(d)] for i in range(len(ans))]

        return ans
```

Using `Reduce`

```python
class Solution:
    def letterCombinations(self, digits):
        if '' == digits: return []
        kvmaps = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        return reduce(lambda acc, digit: [x + y for x in acc for y in kvmaps[digit]], digits, [''])
```
