class Solution:
    ans = -sys.maxsize

    def maxPathSum(self, root):
        self.dfs(root)
        return self.ans

    def dfs(self, root):
        if not root:
            return 0

        left = self.dfs(root.left)
        right = self.dfs(root.right)
        
        val = max(root.val, root.val + left, root.val + right)
        self.ans = max(self.ans, val, root.val + left + right)
        
        return val
