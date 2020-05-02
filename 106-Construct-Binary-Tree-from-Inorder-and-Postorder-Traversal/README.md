# 106 - Construct Binary Tree from Inorder and Postorder Traversal

[leetcode](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)

## Problem

    Given inorder and postorder traversal of a tree, construct the binary tree.
    
    Note:
    You may assume that duplicates do not exist in the tree.
    
    For example, given
    
    inorder = [9,3,15,20,7]
    postorder = [9,15,7,20,3]
    Return the following binary tree:
    
        3
       / \
      9  20
        /  \
       15   7

## Solution

The problem is almost the same as [105 Construct BT from Preorder and Inorder](http://alfmunny.com/leetcode-blog/posts/105-construct-binary-tree-from-preorder-and-inorder-traversal/). Notes can be found there.

```python
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if inorder:
            node = TreeNode(postorder.pop())
            split = inorder.index(node.val)
            node.right = self.buildTree(inorder[split + 1:], postorder)
            node.left = self.buildTree(inorder[:split], postorder)

            return node
```
