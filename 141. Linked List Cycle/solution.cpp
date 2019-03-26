class Solution {
    public:
        bool hasCycle(ListNode *head) {
            if(!head) return false;

            ListNode* slow = head;
            ListNode* fast = head->next;

            while(slow && fast) {
                if(fast == slow)  return true;
                slow = slow->next;
                if(fast->next) fast = fast->next->next;
                else return false;
            }
            return false;
        }
};
