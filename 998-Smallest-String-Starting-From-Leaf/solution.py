class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        self.ans = "~"
        self.dfs(root, [])
        return self.ans
        
    def dfs(self, root, path):
        
        if not root:
            return
        
        path.append(chr(root.val+97))
        
        if not root.left and not root.right:
            self.ans = min(self.ans, "".join(reversed(path)))
    
        self.dfs(root.left, path)
        self.dfs(root.right, path)
        path.pop()
