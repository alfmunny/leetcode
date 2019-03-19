#include <iostream>
#include <vector>


struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
    public:
        TreeNode* mergeTrees(TreeNode* t1, TreeNode* t2) {
            if ( t1 && t2 )
            {
                t1->val = t1->val + t2->val;

                t1->left = mergeTrees(t1->left, t2->left);
                t1->right = mergeTrees(t1->right, t2->right);
            }
            else if ( t1 && t2 == NULL ) return t1;
            else if ( t2 && t1 == NULL ) return t2;

            return t1;
        }
};
