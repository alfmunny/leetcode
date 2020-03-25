#[Unique Paths II](https://leetcode.com/problems/unique-paths-ii/)

## Notes

It is almost the same question of unique paths.
The only difference is to set the value of the obstacle position to zero.

To note that, the initial matrix should be also modified under the consideration of the obstacles.

For example when the 

when there is no obstacle.

The initial dp matrix would be

|1|0|0|
|1|0|0|
|1|0|0|

But when the input matrix has an obstabcle in the first line or first column:

|0|1|0|
|0|0|0|
|0|0|0|

or 

|0|0|0|
|1|0|0|
|0|0|0|

The initial dp matrix would be

|1|0|0|
|1|0|0|
|1|0|0|

or 

|1|1|1|
|0|0|0|
|0|0|0|


1. There are only two possibilities to arrive at the finish point 
    1. arrive at that point from above
    2. arrive at that point from left

2. So the ways to arrive at current point is equal the ways from above plus the ways from left. dp[i][j] = dp[i][j-1] + dp[i - 1][j]. 
dp[i][j] = 0 when an obstacle is at this position.
3. Dynamic programming. Maintain a two dimensional matrix.
4. Complexity O(m * n)