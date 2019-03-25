# 337. House Robber III
Hint: DP

Similar as the house robber in an array problem.

The robber has two options:

1. Rob current node, the child nodes can not be robbed.
2. Do not rob the current node, the grand child nodes can be robbed

root->val + rob(root->left->right) + rob(root->left->left) + rob(root->right->left) + rob(root->right->right)

or

rob(root->left) + rob(root->right)


Steps:

1. Find the recusive relation.
2. Use a map<TreeNode*, int> to avoid overlapping calculations. (Solution1)
3. modify the recursive method to always return an array of these two options
