class Solution:
    def connect(self, root: 'Node') -> 'Node':
        node = root
        while node:
            next_level = node.left
            while node and node.left:
                node.left.next = node.right
                node.right.next = node.next and node.next.left
                node = node.next
            node = next_level
        return root
