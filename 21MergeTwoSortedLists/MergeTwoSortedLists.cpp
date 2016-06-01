#include "MergeTwoSortedLists.h"

ListNode * MergeTwoSortedLists::mergeTwoLists(ListNode * l1, ListNode* l2)
{
	if (!l1)
	{
		return l2;
	}

	if (!l2)
	{
		return l1;
	}

	// extra head node 
	ListNode* l3 = new ListNode(0);
	// attach the l1 to l3
	l3->next = l1;

	ListNode* tmp1 = l1; // moving pointer for l1
	ListNode* tmp2 = l2; // moving pointer for l2
	ListNode* tmp = l3; // moving pointer for l3

	// consider the next node of extra head node, it's actually the first node of l1
	while (tmp->next)
	{
		// when tmp2 is not empty 
		// and the next node of l1 is bigger than current node of l2
		if (tmp2 && tmp->next->val > tmp2->val)
		{
			while (tmp2) 
			{
				// when next node of l1 is still bigger than current node of l2
				// insert the current node into l1
				if (tmp2->val < tmp->next->val)
				{
					l2 = tmp2->next;
				    tmp2->next = tmp->next;
					tmp->next = tmp2;
					tmp2 = l2;
				}
				else
				{
					break;
				}
			}
		}
		// if tmp2 is empty or the next node of l1 is not bigger than the current node of l2
		// move to the next node of l1
		else
		{
			tmp = tmp->next;
		}

	}
	
	// attach the rest of l2 to the l1
	tmp->next = tmp2;

	// remove the extra head node
	tmp = l3;
	l3 = l3->next;
	delete tmp;

	return l3;
}




ListNode * MergeTwoSortedLists::mergeTwoListsRecursive(ListNode * l1, ListNode * l2)
{
	if (!l1)
	{
		return l2;
	}

	if (!l2)
	{
		return l1;
	}
	
	if (l1->val < l2->val)
	{
		ListNode* l3 = mergeTwoListsRecursive(l1->next, l2);
		l1->next = l3;
		return l1;
	}

	else
	{
		ListNode* l3 = mergeTwoListsRecursive(l1, l2->next);
		l2->next = l3;
		return l2;
	}
};