class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        ans = []
        level = [root]
        seen = set(level)
        
        while level:
            new_level = []
            max_val = -float('inf')
            for node in level:
                if node:
                    if node.left:
                        new_level.append(node.left)
                    if node.right:
                        new_level.append(node.right)
                    max_val = max(max_val, node.val)
            ans.append(max_val)
            level = new_level
    
        return ans
