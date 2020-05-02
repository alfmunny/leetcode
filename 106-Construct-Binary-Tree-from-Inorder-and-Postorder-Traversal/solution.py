class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if inorder:
            node = TreeNode(postorder.pop())
            split = inorder.index(node.val)
            node.right = self.buildTree(inorder[split + 1:], postorder)
            node.left = self.buildTree(inorder[:split], postorder)

            return node
