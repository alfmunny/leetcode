#include "solution.h"

using namespace std;

ListNode* Solution::addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* head1 = l1;
        ListNode* head2 = l2;
        ListNode* ret = new ListNode(0);
        ListNode* head3 = ret;
        bool hasCarry = false;
        while(head1 || head2 || hasCarry)
        {

            ListNode* tmp = new ListNode(0);
            head3->next = tmp;
            head3 = head3->next;
            
            if (head1 && head2)
            {
                head3->val = head1->val + head2->val;
                head1 = head1->next;
                head2 = head2->next;
            }
                
            else if (head1)
            {
                head3->val = head1->val;
                head1 = head1->next;
            }
            else if (head2)
            {
                head3->val = head2->val;
                head2 = head2->next;
            }
                
            if ( hasCarry )
            {
                head3->val += 1;
                hasCarry = false;
            }
            
            if(head3->val >= 10)
            {
                head3->val -= 10;
                hasCarry = true;
            }
            
        }
        return ret->next;
};