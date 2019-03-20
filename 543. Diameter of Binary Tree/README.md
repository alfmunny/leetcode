# 543. Diameter of Binary Tree
Remember to keep a global maxium while traverse the tree.
Notice how to calculate the depth of a tree.
```c++
int ret;
int depth(TreeNode* root) 
{
    if (!root) return 0;

    int r = depth(root->right);
    int l = depth(root->left);
    return max(r,l) + 1;
}
```

1. If the path includes the root, then it's depth of right child plus depth of left child plus.
2. If the path does not include the root, then consider the right and left child as root, and repeat the step 1.
