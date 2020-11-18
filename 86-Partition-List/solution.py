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
