#include <iostream>
#include <queue>
#include "108ConvertSortedArrayToBinarySearchTree\sortedArrayToBST.h"

void printTree(TreeNode * root)
{
    if (!root)  return;

    std::queue<TreeNode*> q;
    q.push(root);

    while (! q.empty())
    {
        TreeNode* current = q.front();
        std::cout << current->val << std::endl;
        q.pop();
        if(current->left)
            q.push(current->left);
        if(current->right)
            q.push(current->right);
    }
}

int main() 
{
	vector<int> a = {2, 4, 5, 6};

    TreeNode* root = sortedArrayToBST(a);
    printTree(root);
	system("PAUSE");
	return 0;
}

