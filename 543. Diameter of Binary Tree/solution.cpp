#include <iostream>
#include <algorithm>

class Solution {
    public:
        int diameterOfBinaryTree(TreeNode* root) {
            int ans = 0;
            depth(root, ans);
            return ans;
        }

        int depth(TreeNode* root, int& n) {
            if (!root) return 0;
            int r = depth(root->right, n);
            int l = depth(root->left, n);
            if (n<r+l) n = r+l;
            return std::max(l, r) + 1;
        }
};
