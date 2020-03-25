#[Unique Paths](https://leetcode.com/problems/unique-paths/)

## Notes

1. There are only two possibilities to arrive at the finish point 
    1. arrive at that point from above
    2. arrive at that point from left

2. So the ways to arrive at current point is equal the ways from above plus the ways from left. dp[i][j] = dp[i][j-1] + dp[i - 1][j]
2. Dynamic programming. Maintain a two dimensional matrix.
3. Optimize it to one dimension.
4. Complexity O(m * n)
