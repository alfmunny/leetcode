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
