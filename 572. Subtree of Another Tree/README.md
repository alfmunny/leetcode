# 572. Subtree of Another Tree
1. check from current node if two trees are identical
2. If not identical, check if from the left child or from the right child contains the subtree.

How to check if two trees are identical:

```c++
bool isIdentical(TreeNode* s, TreeNode* t) {
    if (s == NULL && t == NULL) return true;
    if ( !s || !t ) return false;
    return s->val == t->val && isIdentical(s->left, t->left) && isIdentical(s->right, t->right);
}
```
