class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p and not q:
            return False
        if not p and q:
            return False
        if not p and not q:
            return True
        
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False
