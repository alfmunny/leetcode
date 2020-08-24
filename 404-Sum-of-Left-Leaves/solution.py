class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        return self.dfs(root, 0, False)
    
    def dfs(self, root, presum, isLeft):
        if not root:
            return 0
        if not root.left and not root.right and isLeft:
            return presum + root.val
        else:
            return self.dfs(root.left, presum, True) + self.dfs(root.right, presum, False)
