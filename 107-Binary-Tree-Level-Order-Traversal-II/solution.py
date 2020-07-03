class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        stack = []
        while queue:
            next_queue = []
            tmp = []
            while queue:
                n = queue.pop(0)
                tmp.append(n.val)
                if n.left:
                    next_queue.append(n.left)
                if n.right:
                    next_queue.append(n.right)
            stack.append(tmp[:])
            queue = next_queue[:]
            
        return stack[::-1]
