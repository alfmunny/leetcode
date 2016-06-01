#include <iostream>
#include "21MergeTwoSortedLists\MergeTwoSortedLists.h"

int main() 
{
	int a[] = {2, 4, 5, 6};
	int b[] = {1, 1, 1,1,1};

	ListNode* L1 = new ListNode(0);
	ListNode* L2 = new ListNode(0);
	ListNode* End1 = L1;
	ListNode* End2 = L2;
	
	for (int i : a) {
		ListNode* tmp = new ListNode(i);
		End1->next = tmp;
		End1 = End1->next;
	}

	for (int i : b)
	{
		ListNode* tmp = new ListNode(i);
		End2->next = tmp;
		End2 = End2->next;
	}

	MergeTwoSortedLists m;
	ListNode* res = m.mergeTwoLists(L1, L2);

	ListNode* head = res;

	while (head)
	{
		std::cout << head->val << std::endl;
		head = head->next;
	}

	system("PAUSE");
	return 0;
}

