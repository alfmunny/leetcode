class Solution {
    public:
        ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
            ListNode* p1 = headA;
            ListNode* p2 = headB;

            if (!p1 || !p2) return NULL;

            int lenA = 0;
            int lenB = 0;

            while (p1)
            {
                lenA++;
                p1 = p1->next;
            };

            while (p2)
            {
                lenB++;
                p2 = p2->next;
            };

            int lenC = lenA - lenB;
            int len;

            if (lenC > 0)
            {
                p1 = headA;
                p2 = headB;
                len = lenC;
            }
            else
            {
                p1 = headB;
                p2 = headA;
                len = -lenC;
            }

            ListNode* ret = NULL;

            while(len > 0) 
            {
                p1 = p1->next; 
                len--;
            }


            while(p1 && p2)
            {
                if(p1 != p2) 
                {
                    ret = NULL;
                }
                else
                {
                    if(ret == NULL) { ret = p1; }
                }
                p1 = p1->next;
                p2 = p2->next;
            }

            return ret;

        }
};
