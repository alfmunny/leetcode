# 110 - Balanced Binary Tree

[leetcode](https://leetcode.com/problems/balanced-binary-tree/)

## Problem

    Given a binary tree, determine if it is height-balanced.
    
    For this problem, a height-balanced binary tree is defined as:
    
    a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
    
    Example 1:
    
    Given the following tree [3,9,20,null,null,15,7]:
    
        3
       / \
      9  20
        /  \
       15   7
    Return true.
    
    Example 2:
    
    Given the following tree [1,2,2,3,3,null,null,4,4]:
    
           1
          / \
         2   2
        / \
       3   3
      / \
     4   4
    Return false.

## Solution

### Solution 1: multiple pass

```python
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True

        hr = self.height(root.right)
        hl = self.height(root.left)

        return self.isBalanced(root.right) and self.isBalanced(
            root.left) and abs(hr - hl) <= 1

    def height(self, root):
        if not root:
            return 0
        return 1 + max(self.height(root.right), self.height(root.left))
```

### Solution 2: one pass

```python
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.height(root) != -1

    def height(self, root):
        if not root:
            return 0
        lh = self.height(root.right)
        if lh == -1:
            return -1
        rh = self.height(root.left)
        if rh == -1:
            return -1
        if abs(lh - rh) > 1:
            return -1
        return max(lh, rh) + 1

```
