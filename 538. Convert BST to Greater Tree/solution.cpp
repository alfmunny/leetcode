cass Solution {
    public:
        TreeNode* convertBST(TreeNode* root) {
            int sum[1] = {0}; 
            traverse(root, sum);
            return root;
        }

        void traverse(TreeNode* root, int n[]) {

            if (root != NULL )
            {
                traverse(root->right, n);
                n[0] += root->val;
                root->val = n[0];
                traverse(root->left, n);
            }
        }
};
