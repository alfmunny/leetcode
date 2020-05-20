class Solution:
    def kthSmallest(self, root):
        self.k = k
        self.ans = root.val
        traverse(root)
        return self.ans

    def traverse(self, root):
        if not root:
            return
        traverse(root.left)

        self.k -= 1
        if not self.k:
            self.ans = root.val
        else:
            traverse(root.right)
