# 515 - Find Largest Value in Each Tree Row

[leetcode](https://leetcode.com/problems/find-largest-value-in-each-tree-row/)

## Problem

    Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

## Solution

```python
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        ans = []
        level = [root]
        seen = set(level)

        while level:
            new_level = []
            max_val = -float('inf')
            for node in level:
                if node:
                    if node.left:
                        new_level.append(node.left)
                    if node.right:
                        new_level.append(node.right)
                    max_val = max(max_val, node.val)
            ans.append(max_val)
            level = new_level

        return ans
```
