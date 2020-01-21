# 617. [Merge Two Binary Trees](https://leetcode.com/problems/merge-two-binary-trees/)


Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.

Example 1:

Input: 
Tree 1                 Tree 2                  
    1                        2                             
   / \                       / \                            
  3   2                   1   3                        
 /                           \    \                      
5                             4   7                  

Output: 
Merged tree:
         3
        / \
       4   5
      / \   \ 
     5   4   7



Notes:

1. Recursive solution, edit the node in place in the first tree.

```python
  def mergeTrees(self, t1, t2):
    if t1 is None:
      return t2
    if t2 is None:
      return t1

    t1.val += t2.val
    t1.left = self.mergeTrees(t1.left, t2.left)
    t2.right = self.mergeTrees(t1.right, t2.right)

    return t1
```


2. Iterative solution. 
  It's a stack problem to traverse a tree by inorder.
  Push both tree node into stack as pair. Pop them and then edit them.

```python
def mergeTrees(self, t1, t2):
    if not t1:
        return t2
    
    stack = [[t1, t2]]
    
    while(stack):
        t = stack.pop()

        # Both must not be null. 
        if (not t[0] or not t[1]):
            continue
            
        t[0].val += t[1].val
        
        if not t[0].left:
          	# From here, no need to push to the stack
            t[0].left = t[1].left
        else:
            stack.append([t[0].left, t[1].left])
            
        if not t[0].right:
          	# From here, no need to push to the stack
            t[0].right = t[1].right
        else:
            stack.append([t[0].right, t[1].right])
            
    return t1
```
