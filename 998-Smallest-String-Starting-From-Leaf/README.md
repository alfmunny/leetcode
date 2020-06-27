# 988 - Smallest String Starting From Leaf

[leetcode](https://leetcode.com/problems/smallest-string-starting-from-leaf/)

## Problem

    Given the root of a binary tree, each node has a value from 0 to 25 representing the letters 'a' to 'z': a value of 0 represents 'a', a value of 1 represents 'b', and so on.
    
    Find the lexicographically smallest string that starts at a leaf of this tree and ends at the root.
    
    (As a reminder, any shorter prefix of a string is lexicographically smaller: for example, "ab" is lexicographically smaller than "aba".  A leaf of a node is a node that has no children.
    
    Example 1:
    
    Input: [0,1,2,3,4,3,4]
    Output: "dba"
    
    Example 2:
    
    Input: [25,1,3,1,3,0,2]
    Output: "adz"

## Solution

```python
class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        self.ans = "~"
        self.dfs(root, [])
        return self.ans

    def dfs(self, root, path):

        if not root:
            return

        path.append(chr(root.val+97))

        if not root.left and not root.right:
            self.ans = min(self.ans, "".join(reversed(path)))

        self.dfs(root.left, path)
        self.dfs(root.right, path)
        path.pop()
```
