#pragma once

struct ListNode {
	int val;
	ListNode *next;
	ListNode(int x) : val(x), next(nullptr) { }
};

class MergeTwoSortedLists {
public:
	ListNode* mergeTwoLists(ListNode* l1, ListNode* l2);
	ListNode* mergeTwoListsRecursive(ListNode* l1, ListNode* l2);
};