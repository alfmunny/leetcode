class Solution:
    def isSymmetric(self, root):
        if not root:
            return True
        return self.isMirrored(root.left, root.right)

    def isMirrored(self, left, right):

        if not left and not right:
            return True
        elif not left:
            return False
        elif not right:
            return False
        else:
            if left.val == right.val:
                return self.isMirrored(left.left, right.right) and \
                    self.isMirrored(left.right, right.left)
            else:
                return False
print("THIS")
print("THIS")
print("THIS")
