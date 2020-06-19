class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        first = head
        second = first.next
        
        while second:
            if first.val == second.val:
                first.next = second.next
                second = first.next
            else:
                first, second = second, second.next
        
        return head
