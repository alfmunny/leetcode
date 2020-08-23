class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        ans = []
        self.print(root, ans, 0)
        return ans
    
    def print(self, root, ans, depth):
        if not root:
            return
        
        if depth + 1 > len(ans): ans.append(root.val)
        
        self.print(root.right, ans, depth+1)
        self.print(root.left, ans, depth+1)
