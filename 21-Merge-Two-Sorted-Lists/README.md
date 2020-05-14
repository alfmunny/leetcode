# 21 - Merge Two Sorted Lists

[leetcode](https://leetcode.com/problems/merge-two-sorted-lists/)

## Problem

    Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
         
    Example:
         
    Input: 1->2->4, 1->3->4
    Output: 1->1->2->3->4->4

## Notes

Recursion is your friend!

## Solution

### Solution 1: Recursive

```python
class Solution:
    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1

        if l1.val > l2.val:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
        else:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
```
