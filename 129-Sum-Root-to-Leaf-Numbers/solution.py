# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0

        self.ans = 0
        self.dfs(root, [])
        return self.ans

    def dfs(self, root, path):
        if not root:
            return

        if not root.right and not root.left:
            path.append(root.val)
            self.ans += int("".join([str(i) for i in path]))
            path.pop()
            return

        path.append(root.val)
        self.dfs(root.left, path)
        self.dfs(root.right, path)
        path.pop()
