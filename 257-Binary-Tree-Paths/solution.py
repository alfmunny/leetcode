class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        
        if not root.right and not root.left:
            return [str(root.val)]
        
        paths = [str(root.val) + "->" + s for s in self.binaryTreePaths(root.right) + self.binaryTreePaths(root.left)]
        return paths
