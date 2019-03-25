# 198. House Robber

The robber has two options:

1. robe the current house, the previous house can not be robbed.
2. robe the previous house, but not the current.

The max value must be one of them.

robe(i) = max(robe(i-2) + currentValue, robe(i-1));

Mind steps of DP problem:

1. Find the recurisve relations and write the solution.
2. Use a memory array to avoid calculate the result multiple times. 
3. Improve it with non-recurisve solution.
