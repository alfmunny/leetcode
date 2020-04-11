class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        elif not root.right and not root.left:
            return 0
        elif not root.right:
            return max(self.diameterOfBinaryTree(root.left),
                       1 + self.height(root.left))
        elif not root.left:
            return max(self.diameterOfBinaryTree(root.right),
                       1 + self.height(root.right))
        else:
            return max(self.diameterOfBinaryTree(root.right),
                       self.diameterOfBinaryTree(root.left),
                       self.height(root.left) + self.height(root.right) + 2)

    def height(self, root):

        if not root:
            return 0
        if not root.right and not root.left:
            return 0

        return 1 + max(self.height(root.left), self.height(root.right))
