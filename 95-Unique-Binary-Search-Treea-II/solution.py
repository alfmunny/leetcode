class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        return self.helper(1, n+1)
        
    def helper(self, start, end):
        if start >= end:
            return [None]
        res = []
        for i in range(start, end):
            for left in self.helper(start, i):
                for right in self.helper(i+1, end):
                    node = TreeNode(i)
                    node.left, node.right = left, right
                    res.append(node)
        return res
