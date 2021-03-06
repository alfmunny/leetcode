# 82 - Remove Duplicates from Sorted List II

[leetcode](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/)

## Problem

    Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.
    
    Return the linked list sorted as well.
    
    Example 1:
    
    Input: 1->2->3->3->4->4->5
    Output: 1->2->5
    Example 2:
    
    Input: 1->1->1->2->3
    Output: 2->3

## Solution

```python
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        extra = ListNode(None)

        extra.next = head
        pre = extra

        while head and head.next:
            if head.val == head.next.val:
                while head and head.next and head.val == head.next.val:
                    head = head.next

                head = head.next
                pre.next = head
            else:
                pre = head
                head = head.next

        return extra.next
```
