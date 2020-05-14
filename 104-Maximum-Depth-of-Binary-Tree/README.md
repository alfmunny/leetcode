# 104 - Maximum Depth of Binary Tree

[leetcode](https://leetcode.com/problems/maximum-depth-of-binary-tree/)

## Problem

    Given a binary tree, find its maximum depth.
         
    The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
         
    Note: A leaf is a node with no children.
         
    Example:
         
    Given binary tree [3,9,20,null,null,15,7],
         
        3
       / \
      9  20
        /  \
       15   7

## Notes

Recursion is your friend!

## Solution

\#+begin\_src python class Solution: def maxDepth(self, root): return 1 + max(self.maxDepth(root.right), self.maxDepth(
