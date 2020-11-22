# 257 - Binary Tree Paths

[leetcode](https://leetcode.com/problems/binary-tree-paths/)

## Problem

    iven a binary tree, return all root-to-leaf paths.
    
    Note: A leaf is a node with no children.
    
    Example:
    
    Input:
    
       1
     /   \
    2     3
     \
      5
    
    Output: ["1->2->5", "1->3"]
    
    Explanation: All root-to-leaf paths are: 1->2->5, 1->3

## Solution

```python
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []

        if not root.right and not root.left:
            return [str(root.val)]

        paths = [str(root.val) + "->" + s for s in self.binaryTreePaths(root.right) + self.binaryTreePaths(root.left)]
        return paths
```
