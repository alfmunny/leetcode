class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        # split in half
        fast = slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        
        second = slow.next
        slow.next = None
        
        first = self.sortList(head)
        second = self.sortList(second)
        
        # merge
        return self.merge(first, second)
        
    def merge(self, p1, p2):
        p = dummy = ListNode(0)
        
        while p1 and p2:
            if p1.val < p2.val:
                p.next, p1 = p1, p1.next
            else:
                p.next, p2 = p2, p2.next
            p = p.next
                
        p.next = p1 or p2
            
        return dummy.next
