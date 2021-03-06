# 116 - Populating Next Right Pointers in Each Node

[leetcode](https://leetcode.com/problems/populating-next-right-pointers-in-each-node/)

## Problem

    You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:
    
    struct Node {
      int val;
      Node *left;
      Node *right;
      Node *next;
    }
    Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
    
    Initially, all next pointers are set to NULL.
    
    Follow up:
    
    You may only use constant extra space.
    Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.

## Solution

Constant Space

```python
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        node = root
        while node:
            next_level = node.left
            while node and node.left:
                node.left.next = node.right
                node.right.next = node.next and node.next.left
                node = node.next
            node = next_level
        return root
```
