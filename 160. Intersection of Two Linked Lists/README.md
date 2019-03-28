# 160. Intersection of Two Linked Lists

Write a program to find the node at which the intersection of two singly linked lists begins.

1. Check the length of both list.
2. Start comparing at the point that two list have the same length

Example:

A = [4,1,8,4,5]
B = [5,0,1,8,4,5]

lenA = 5
lenB = 6

Move the pointer of B to 0, start comparing with A. They have both same length now.
