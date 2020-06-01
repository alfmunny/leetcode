# 226 - Invert Binary Tree

[leetcode](https://leetcode.com/problems/invert-binary-tree/)

## Problem

    Invert a binary tree.
    
    Example:
    
    Input:
    
         4
       /   \
      2     7
     / \   / \
    1   3 6   9
    Output:
    
         4
       /   \
      7     2
     / \   / \
    9   6 3   1

## Solution

```python
class Solution:
    def invertTree(self):
        if root:
            tmp = root.left
            root.left = self.invertTree(root.right)
            root.right = self.invertTree(tmp)
        return root
```
