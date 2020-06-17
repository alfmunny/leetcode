# 100 - Same Tree

[leetcode](https://leetcode.com/problems/same-tree/)

## Problem

    Given two binary trees, write a function to check if they are the same or not.
    
    Two binary trees are considered the same if they are structurally identical and the nodes have the same value.
    
    Example 1:
    
    Input:     1         1
              / \       / \
             2   3     2   3
    
            [1,2,3],   [1,2,3]
    
    Output: true
    Example 2:
    
    Input:     1         1
              /           \
             2             2
    
            [1,2],     [1,null,2]
    
    Output: false
    Example 3:
    
    Input:     1         1
              / \       / \
             2   1     1   2
    
            [1,2,1],   [1,1,2]
    
    Output: false

## Solution

```python
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p and not q:
            return False
        if not p and q:
            return False
        if not p and not q:
            return True

        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False

```
