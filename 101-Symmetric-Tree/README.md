
# 101 - Symmetric Tree

[leetcode](https://leetcode.com/problems/symmetric-tree/)


## Problem

    Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
    
    For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
    
        1
       / \
      2   2
     / \ / \
    3  4 4  3
     
    
    But the following [1,2,2,null,3,null,3] is not:
    
        1
       / \
      2   2
       \   \
       3    3


## Notes

Recursion !


## Solution


### Solution 1: recursive

    class Solution:
        def isSymmetric(self, root):
            if not root:
                return True
            return self.isMirrored(root.left, root.right)
    
        def isMirrored(self, left, right):
    
            if not left and not right:
                return True
            elif not left:
                return False
            elif not right:
                return False
            else:
                if left.val == right.val:
                    return self.isMirrored(left.left, right.right) and \
                        self.isMirrored(left.right, right.left)
                else:
                    return False


### TODO Solution 2: How to solve it non recursively

