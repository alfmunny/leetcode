class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        
        ans = []
        self.dfs(root, sum, [], ans)
        return ans
         
    def dfs(self, root, sum, path, ans):
        
        if not root:
            return
        
        path.append(root.val)
        if root.val == sum and not root.right and not root.left:
            ans.append(list(path))
        self.dfs(root.left, sum - root.val, path, ans)
        self.dfs(root.right, sum - root.val, path, ans)
        path.pop()
