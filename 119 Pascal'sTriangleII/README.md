# [119. Pascal's Triangle II](https://leetcode.com/problems/pascals-triangle-ii/)

Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?


## Notes:

1. It's a dynamic programming problem.

    always move the previous array forward by one step and add it to itself

    ```
    1
    + 1 
    = 1, 1
    +    1, 1
    = 1, 2, 1
    +    1, 2, 1
    = 1, 3, 3, 1
    ```

2. Prepare an array of 1s, and loop it through.

3. Complexity O(N^2); 