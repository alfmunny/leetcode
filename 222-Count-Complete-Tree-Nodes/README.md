# 222 - Count Complete Tree Nodes

[leetcode](https://leetcode.com/problems/count-complete-tree-nodes/)

## Problem

    Given a complete binary tree, count the number of nodes.
    
    Note:
    
    Definition of a complete binary tree from Wikipedia:
    In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.
    
    Example:
    
    Input: 
        1
       / \
      2   3
     / \  /
    4  5 6
    
    Output: 6

## Solution

```python
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        rd = self.height(root.right)
        ld = self.height(root.left)

        if rd == ld:
            return pow(2, ld) + self.countNodes(root.right)
        else:
            return pow(2, rd) + self.countNodes(root.left)

    def height(self, root):
        if not root:
            return 0

        return 1 + self.height(root.left)
```
