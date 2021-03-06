# 235 - Lowest Common Ancestor of a Binary Search Tree

[leetcode](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)

## Problem

    Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
    
    According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
    
    Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
    Output: 6
    Explanation: The LCA of nodes 2 and 8 is 6.

## Solution

```python
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root and (p.val-root.val) * (q.val-root.val) > 0:
            if p.val - root.val < 0:
                root = root.left
            else:
                root = root.right
        return root        
```
