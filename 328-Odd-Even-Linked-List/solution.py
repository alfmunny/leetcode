class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next or not head.next.next:
            return head
        
        p1, p2 = head, head.next
        even = p2
        
        while p2 and p2.next:
            p1.next = p2.next                
            p1 = p1.next
            p2.next = p1.next
            p2 = p2.next

        p1.next = even
    
        return head
