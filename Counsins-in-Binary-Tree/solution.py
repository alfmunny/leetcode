class Solution:
    m = {}

    def isCousins(self, root, x, y):
        if not root:
            return False

        if self.depth(root, x) == self.depth(root, y):
            return self.m[x] != self.m[y]

        return False

    def depth(self, root, val):
        if not root:
            return -1

        if root.val == val:
            return 0
        else:

            left = self.depth(root.left, val)
            right = self.depth(root.right, val)

            if left >= 0:
                self.m[root.left.val] = root.val
                return 1 + left
            elif right >= 0:
                self.m[root.right.val] = root.val
                return 1 + right

        return -1
