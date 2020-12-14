class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root and (p.val-root.val) * (q.val-root.val) > 0:
            if p.val - root.val < 0:
                root = root.left
            else:
                root = root.right
        return root
