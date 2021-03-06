# 107 - Binary Tree Level Order Traversal II

[leetcode](https://leetcode.com/problems/binary-tree-level-order-traversal-ii/)

## Problem

    Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).
    
    For example:
    Given binary tree [3,9,20,null,null,15,7],
        3
       / \
      9  20
        /  \
       15   7
    return its bottom-up level order traversal as:
    [
      [15,7],
      [9,20],
      [3]
    ]

## Solution

```python
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        stack = []
        while queue:
            next_queue = []
            tmp = []
            while queue:
                n = queue.pop(0)
                tmp.append(n.val)
                if n.left:
                    next_queue.append(n.left)
                if n.right:
                    next_queue.append(n.right)
            stack.append(tmp[:])
            queue = next_queue[:]

        return stack[::-1]
```
