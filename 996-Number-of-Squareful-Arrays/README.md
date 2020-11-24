# 996 - Number of Squareful Arrays

[leetcode](https://leetcode.com/problems/number-of-squareful-arrays/)

## Problem

    Given an array A of non-negative integers, the array is squareful if for every pair of adjacent elements, their sum is a perfect square.
    
    Return the number of permutations of A that are squareful.  Two permutations A1 and A2 differ if and only if there is some index i such that A1[i] != A2[i].
    
     
    
    Example 1:
    
    Input: [1,17,8]
    Output: 2
    Explanation: 
    [1,8,17] and [17,8,1] are the valid permutations.
    Example 2:
    
    Input: [2,2,2]
    Output: 1
     
    
    Note:
    
    1 <= A.length <= 12
    0 <= A[i] <= 1e9

## Solution

Simple DFS

```python
class Solution:
    def numSquarefulPerms(self, A: List[int]) -> int:
        self.h = defaultdict(bool)

        mark = [False] * len(A)
        self.ret = 0
        self.dfs(sorted(A), [], mark)
        return self.ret 

    def dfs(self, A, path, mark):

        if len(path) == len(A):
            self.ret += 1

        for i, v in enumerate(A):
            if (i > 0 and A[i] == A[i-1] and not mark[i-1]) or mark[i]:
                continue
            if not path or self.isSquare(path[-1]+v):
                mark[i] = True
                self.dfs(A, path+[v], mark)
                mark[i] = False

    def isSquare(self, num):
        return True if int((num**0.5))**2 == num else False
```
