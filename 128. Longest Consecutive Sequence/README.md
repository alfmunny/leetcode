# 128. Longest Consecutive Sequence

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.


Notes:

1. Use a map to track the max length on the boundaries.
2. Only need to remember the max length of the boundaries.
3. Only update the boundaries when the boundaries got extended.

```
map;
ret = 0;

for (int n : nums)
    if (m[n]) 
        continue; /*not the boundary */
    else /* otherwise the element n is a boundary */
        left = m[n-1]; # left boundary, could be 0
        right = m[n+1]; # right boundary, could be 0
        m[0] = left + right + 1; # new length

        m[n - left] = m[0]; # find the left boundary and update it
        m[n + right] = m[0]; # find the right boundary and update it.

        ret = max(ret, m[n]);
```


