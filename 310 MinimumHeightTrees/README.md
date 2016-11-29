#[330 Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/)

## Notes:
1. Replace the element of subsequence if the current element is smaller than the largest one.

1, 4, 5, 6, 3, 7

1
1, 4
1, 4, 5,
1, 4, 5, 6,
1, 3, 5, 6
1, 3, 5, 6, 7

The trick is, the subsequence will not be exactly the acutal subsequence, but the length is always right.

In this way we can always replace the element by using binary tree search.

Complexity: O(NlogN)