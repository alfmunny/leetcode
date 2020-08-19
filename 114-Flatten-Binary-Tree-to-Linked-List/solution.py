class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.pre = None
        self.dfs(root)
        
    def dfs(self, root):
        
        if not root:
            return
        
        self.dfs(root.right)
        self.dfs(root.left)
        
        root.right = self.pre
        self.pre = root
        root.left = None
