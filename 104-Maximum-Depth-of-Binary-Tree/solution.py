class Solution:
    def maxDepth(self, root):
        return 1 + max(self.maxDepth(root.right), self.maxDepth(root.left)) if root else 0
