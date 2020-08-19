class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.height(root) != -1

    def height(self, root):
        if not root:
            return 0
        lh = self.height(root.right)
        if lh == -1:
            return -1
        rh = self.height(root.left)
        if rh == -1:
            return -1
        if abs(lh - rh) > 1:
            return -1
        return max(lh, rh) + 1
