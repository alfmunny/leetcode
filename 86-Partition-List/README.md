# 86 - Partition List

[leetcode](https://leetcode.com/problems/partition-list/)

## Problem

    Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
    
    You should preserve the original relative order of the nodes in each of the two partitions.
    
    Example:
    
    Input: head = 1->4->3->2->5->2, x = 3
    Output: 1->2->2->4->3->5

Notes:

Two pointers:

p1: mark the end of smaller part

p2: go forward to find the smaller one and swap with p1.next

Addtional prev pointer for the swap.

1.  Use a dummy node to make it possible to swap the smaller one to the head
2.  Note the case when p1 == prev, no need to swap, just move p1 forward

## Solution

```python
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        head = ListNode(0, head)

        p1, prev, p2 = head, head, head.next

        while p2:
            if p2.val < x:
                if p1 == prev:
                    prev, p2 = p2, p2.next
                else:
                    p1.next, p2.next, p2, prev.next = p2, p1.next, p2.next, p2.next
                p1 = p1.next
            else:
                prev, p2 = p2, p2.next

        return head.next
```
