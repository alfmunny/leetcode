#include "sortedArrayToBST.h"
#include <iostream>

TreeNode* sortedArrayToBST(vector<int>& nums) 
{
    if (nums.size() == 0)
    {
        return NULL;
    }

    int index = nums.size() / 2;

    TreeNode* root = new TreeNode(nums[index]);

    vector<int> vector_left(nums.begin(), nums.begin() + index);
    vector<int> vector_right(nums.begin() + index + 1, nums.end());

    TreeNode* left = sortedArrayToBST(vector_left);
    TreeNode* right = sortedArrayToBST(vector_right);

    root->left = left;
    root->right = right;

    return root;
}

TreeNode* sortedArrayToBSTRecursive(vector<int>& nums, int l, int r) 
{
    if (nums.size() == 0 || r > nums.size() - 1 || l < 0)
    {
        return NULL;
    }

    int index = l + (r - l + 1) / 2;

    TreeNode* root = new TreeNode(nums[index]);
    
    int l_index = index - 1;
    int r_index = index + 1;
    
    TreeNode* left = sortedArrayToBSTRecursive(nums, l, l_index);
    TreeNode* right = sortedArrayToBSTRecursive(nums, r_index, r);

    root->left = left;
    root->right = right;

    return root; 
}
