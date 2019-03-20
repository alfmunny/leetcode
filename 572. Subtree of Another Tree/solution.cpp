/**
  Definition for a binary tree node.
  struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode(int x) : val(x), left(NULL), right(NULL) {}
  };
*/

class Solution {
    public:
        bool isSubtree(TreeNode* s, TreeNode* t) {
            if (s) return isIdentical(s,t) || isSubtree(s->right, t) || isSubtree(s->left, t);
            else return false;
        }

        bool isIdentical(TreeNode* s, TreeNode* t) {
            if (!s && !t ) return true;
            if ( !s || !t ) return false;
            return s->val == t->val && isIdentical(s->left, t->left) && isIdentical(s->right, t->right);
        }
};
