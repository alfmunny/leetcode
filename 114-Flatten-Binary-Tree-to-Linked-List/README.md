# 114 - Flatten Binary Tree to Linked List

[leetcode](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/)

## Problem

    Given a binary tree, flatten it to a linked list in-place.
    
    For example, given the following tree:
    
        1
       / \
      2   5
     / \   \
    3   4   6
    The flattened tree should look like:
    
    1
     \
      2
       \
        3
         \
          4
           \
            5
             \
              6

## Solution

1.  Traverse the tree in reverse preorder, the opposite of root-left-right.
2.  Save the root, and use it in the upper level.

```python
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.pre = None
        self.dfs(root)

    def dfs(self, root):

        if not root:
            return

        self.dfs(root.right)
        self.dfs(root.left)

        root.right = self.pre
        self.pre = root
        root.left = None
```
