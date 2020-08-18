# 109 - Convert Sorted List to Binary Search Tree

[leetcode](https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/)

## Problem

    Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
    
    For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

## Solution

```python
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)

        slow = head
        fast = head.next.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        tmp = slow.next
        slow.next = None

        root = TreeNode(tmp.val)

        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(tmp.next)

        return root
```
