class Solution(object):
    def __init__(self):
        self.map = {}

    def buildTree(self, preorder, inorder):
        for i, val in enumerate(inorder):
            self.map[val] = i

        return self.recursive(0, len(preorder) - 1, preorder, inorder)

    def recursive(self, start, end, preorder, inorder):
        if (start > end):
            return None

        node = TreeNode(preorder.pop(0))

        split = self.map[node.val]

        node.left = self.recursive(start, split - 1, preorder, inorder)
        node.right = self.recursive(split + 1, end, preorder, inorder)

        return node
