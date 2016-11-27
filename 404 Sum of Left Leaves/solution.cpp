#include "solution.h"

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

int Solution::sumOfLeftLeaves(TreeNode* root) {
        if(!root) return 0;
        if(root->left && !root->left->left && !root->left->right) return root->left->val + sumOfLeftLeaves(root->right);
        else return sumOfLeftLeaves(root->right) + sumOfLeftLeaves(root->left);
    }
};
