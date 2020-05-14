#include <iostream>
#include <vector>

class Solution1 {
    public:

        std::unordered_map<TreeNode*, int> map;

        int rob(TreeNode* root) {

            if(!root) return 0;

            if(map[root]) return map[root];

            int ans = 0;

            if (root->left) ans += rob(root->left->right) + rob(root->left->left);

            if (root->right) ans += rob(root->right->right) + rob(root->right->left);

            ans = max(root->val + ans, rob(root->left) + rob(root->right));

            map[root] = ans;

            return ans;
        }
};


class Solution2 {
    public:

        int rob(TreeNode* root) {
            vector<int> ans = robSub(root);
            return std::max(ans[0], ans[1]);
        }

        vector<int> robSub(TreeNode* root) {
            int vector<int> ans = {0, 0};
            if (!root) return ans;

            vector<int> left = robSub(root->left);
            vector<int> right = robSub(root->right);

            ans[0] = root->val + left[1] + right[1];
            ans[1] = std::max(left[0], left[1]) + std::max(right[0], right[1]);
            return ans;
        }
}


