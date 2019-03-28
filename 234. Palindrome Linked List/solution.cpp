#include <iostream>

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
    public: 
        bool isPalindrome(ListNode* head) {

            ListNode* p1 = head;
            ListNode* p2 = reverseList(head);
            while(p1 && p2)
            {
                if (p1->val == p2->val) 
                {
                    p1 = p1->next;
                    p2 = p2->next;
                }
                else
                {
                    return false;
                }
            }

            return true;
        }

        ListNode* reverseList(ListNode* head) {
            ListNode* p1 = head;
            ListNode* p2 = NULL;

            while (p1)
            {
                ListNode* tmp = new ListNode(p1->val);
                tmp->next = p2;
                p2 = tmp; 
                p1 = p1->next;
            }

            return p2;
        }
};

int main() {
    Solution x;

    ListNode one(1);
    ListNode two(2);
    ListNode three(2);
    ListNode four(1);
    one.next = &two;
    two.next = &three;
    three.next = &four;
    ListNode* head = &one;
    ListNode* p1 = &one;
    ListNode* haha = x.reverseList(head);

    while (p1)
    {
        std::cout << p1->val << " ";
        p1= p1->next;
    }

    while (haha)
    {
        std::cout << haha->val << " ";
        haha = haha->next;
    }

    std::cout << x.isPalindrome(&one) << " ";

    return 0;

}

