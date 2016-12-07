#include "partition_list.h"

ListNode * Solution::partition(ListNode * head, int x)
{
    ListNode* left = new ListNode(0);
    ListNode* left_p = left;
    ListNode* right = new ListNode(0);
    ListNode* right_p = right;
    
    ListNode* root = head;
    
    while(root)
    {
        if(root->val < x) 
        {
            left_p->next = new ListNode(root->val);
            left_p = left_p->next;
        }
        
        else
        {
            right_p->next = new ListNode(root->val);
            right_p = right_p->next;
        }
        root = root->next;
    }
    
    left_p->next = right->next;
    
    if(!left->next) return right->next;
    else return left->next;
}
