class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        
        slow = head
        fast = head.next.next
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        tmp = slow.next
        slow.next = None
        
        root = TreeNode(tmp.val)
        
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(tmp.next)
        
        return root
