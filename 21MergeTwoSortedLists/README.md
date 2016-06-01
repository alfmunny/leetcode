# [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)

Difficulty: Easy

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Notes:

1. Complexity: O(n)
2. Three way to solve it:
	a. Make a new list, compare all the elements, and attach the smaller one to the list (Solved)
	b. L1 Inplace, find the suitable segment in L2, then insert the whole segment into L1, this method should be faster, because it has less pointer opertations.
	c. Recursivly, two cases, if the current node of L1 is smaller, then merge the L1 from next node and L2, and attach the merged list to current node.
	if the current node of l2 is smaller, then merge the l2 from next node and l1, and attach the merged list to current node. (Solved)
3. Have a virtual head node to simplify the problem.