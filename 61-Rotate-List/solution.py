# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not k:
            return head
        
        first = second = head
        
        count = 0
        
        while first:
            count += 1
            first = first.next
            
        k = k % count
        first = head
        
        for i in range(k):
            first = first.next
            
        while first.next:
            first = first.next
            second = second.next
            
        first.next = head
        head = second.next
        second.next = None
        
        return head
