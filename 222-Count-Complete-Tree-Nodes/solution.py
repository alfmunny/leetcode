class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        rd = self.height(root.right)
        ld = self.height(root.left)

        if rd == ld:
            return pow(2, ld) + self.countNodes(root.right)
        else:
            return pow(2, rd) + self.countNodes(root.left)

    def height(self, root):
        if not root:
            return 0

        return 1 + self.height(root.left)
