class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        
        if not root:
            return None
        
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                root = root.right
            elif not root.right:
                root = root.left
            else:
                node = self.getMin(root.right)
                node.left = root.left
                root = root.right
            
        return root
    
    def getMin(self, root):
        if not root:
            return None
        
        return self.getMin(root.left) or root
