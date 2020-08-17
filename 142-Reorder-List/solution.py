class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head or not head.next:
            return
        fast = slow = head
        
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            
        p1, p2 = slow, slow.next
        slow.next = None
        
        while p2:
            p2.next, p2, p1 = p1, p2.next, p2
        
        first = head
        tail = p1
        
        while tail and first:
            
            first.next, tail.next, first, tail = tail, first.next, first.next, tail.next
