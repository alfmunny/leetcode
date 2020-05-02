class Solution:
    def isValidBST(self, root):
        return self.isValidBSTBound(root, -sys.maxsize, sys.maxisze)

    def isValidBSTBound(self, root, lb, hb):
        if not root:
            return True

        if lb < root.val < hb:
            return self.isValidBSTBound(root.left, lb, root.val) and self.isValidBSTBound(root.right, root.val, hb)
        else:
            return False
