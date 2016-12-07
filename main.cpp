#include <iostream>
#include <queue>
#include <ctime>
#include <map>
#include <stack>
#include "86 Partition List\partition_list.h"

int main()
{
    //vector<int> a = { 1, 2, 3, 10, 100, 77, 1,2,34,45,654,234,12,312,45,43};
    std::string s = "[()]{";

    time_t start = time(NULL);
    Solution x;
    std::string ransomNote = "aa";
    std::string magazine = "ab";
    ListNode* head = new ListNode(8);
    ListNode* p = head;
    p->next = new ListNode(4);
    p = p->next;
    p->next = new ListNode(2);
    p = p->next;
    p->next = new ListNode(3);
    p = p->next;

    p = head;

    while (p)
    {
        std::cout << p->val << ", ";
        p = p->next;
    }

    // -1 -2147483648

    ListNode* ret = x.partition(head, 3);
    p = ret;

    std::cout << std::endl;

    while (p)
    {
        std::cout << p->val << ", ";
        p = p->next;
    }


    time_t end = time(NULL);

    //std::cout << double(end - start) / CLOCKS_PER_SEC << std::endl;

	system("PAUSE");
    return 0;
}