class Solution:
    pos = 0
    def bstFromPreorder(self, preorder, bound=float('inf')):
        if self.pos >= len(preorder) or preorder[self.pos] > bound:
            return None
        root = TreeNode(preorder[self.pos])
        self.pos += 1
        root.left = self.bstFromPreorder(preorder, root.val)
        root.right = self.bstFromPreorder(preorder, bound)
        return root
