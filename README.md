
# LeetCode


# Table of Contents

-   [LeetCode](#orgcda51e8)
    -   [41 - First Missing Positive](#orga6c731e)
    -   [48 - Rotate Image](#org575bd4b)
    -   [53 - Maximum Subarray](#org18f24d4)
    -   [55 - Jump Game](#orgce7eaa6)
    -   [62 - Unique Paths](#orgfe08b35)
    -   [64 - Minimum Path Sum](#orgfe70ebe)
    -   [70 - Climbing Stairs](#org6b85062)
    -   [91 - Decode Ways](#org998a903)
    -   [509 - Fibonacci Number](#org3e9f584)
    -   [75 - Sort Colors](#orgb4b62c9)
    -   [78 - Subsets](#orgb2fdd47)
    -   [79 - Word Search](#orgade3b8e)
    -   [45 - Jump Game II](#org177a595)
    -   [1306 - Jump Game III](#org4b122a4)
    -   [84 - Largest Rectangle in Histogram](#org3cfebe9)
    -   [85 - Maximal Rectangle](#org23ce5eb)
    -   [121 - Best Time to Buy and Sell Stock](#org8faa9e8)
    -   [122 - Best Time to Buy and Sell Stock II](#orga0f7a9f)
    -   [123 - Best Time to Buy and Sell Stock III](#org6d99ebf)
    -   [188 - Best Time to Buy and Sell Stock IV](#org895dda4)
    -   [309 - Best Time to Buy and Sell Stock with Cooldown](#orge52e1b3)
    -   [104 - Maximum Depth of Binary Tree](#org27b3f8c)
    -   [21 - Merge Two Sorted Lists](#org967a7f4)
    -   [101 - Symmetric Tree](#org00dd672)
    -   [198 - House Robber](#orgc3e81fc)
    -   [300 - Longest Increasing Subsequence](#org74ed72b)
    -   [322 - Coin Change](#org3e33279)


<a id="orga6c731e"></a>

## 41 - First Missing Positive


### Problem

    Given an unsorted integer array, find the smallest missing positive integer.
    
    Example 1:
    
    Input: [1,2,0]
    Output: 3
    
    Example 2:
    
    Input: [3,4,-1,1]
    Output: 2
    
    Example 3:
    
    Input: [7,8,9,11,12]
    Output: 1
    
    Note:
    
    Your algorithm should run in O(n) time and uses constant extra space.


### Notes

Run in O(n) time and uses constant extra space

1.  Say the length of the array is l, the number must be in 1&#x2026;l+1 (also l possible numbers)
    
    For example 
    
    [1, 2, 3, 4], the first missing positive is 5.
    
    [7, 8, 9, 10], the first missing positive is 1
    
    It means you can use the array as a constant space. The result must be (one of the indexes + 1).

2.  We put the number in the right place. When it is 10, we swap it with A[9].

After all the numbers are in the right place, the first one, whose index + 1 != number, it is the missing one

-   How to put the numer in the right place

    Use the \`while\` to swap the numbers. Only \`if\` can not do the same job.
    
    Consider nums = [3, 4, -1, 1].
    
    Only with if:
    
    First Loop: swap 3 and -1
    
    nums = [-1, 4, 3, 1]
    
    Second Loop: swap 4 and 1
    
    nums = [-1, 1, 3, 4]
    
    And the process stops. Because 4 is already in the right place. You miss to put the 1 in the right place.
    
    So you have to do it recursively, with \`while\`.


### Solution

    class Solution(object):
        def firstMissingPositive(self, nums):
            l = len(nums)
            for i in range(l):
                # Note!: here has to be using while
                while (nums[i] > 0 and nums[i] <= l and nums[nums[i] - 1] != nums[i]):
                    nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
    
            for i, n in enumerate(nums):
                if (n != i+1):
                    return i + 1
    
            return l + 1


<a id="org575bd4b"></a>

## 48 - Rotate Image

[leetcode](https://leetcode.com/problems/rotate-image/)


### Problem

    You are given an n x n 2D matrix representing an image.
    
    Rotate the image by 90 degrees (clockwise).
    
    Note:
    
    You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
    
    Example 1:
    
    Given input matrix = 
    [
      [1,2,3],
      [4,5,6],
      [7,8,9]
    ],
    
    rotate the input matrix in-place such that it becomes:
    [
      [7,4,1],
      [8,5,2],
      [9,6,3]
    ]
    Example 2:
    
    Given input matrix =
    [
      [ 5, 1, 9,11],
      [ 2, 4, 8,10],
      [13, 3, 6, 7],
      [15,14,12,16]
    ], 
    
    rotate the input matrix in-place such that it becomes:
    [
      [15,13, 2, 5],
      [14, 3, 4, 1],
      [12, 6, 8, 9],
      [16, 7,10,11]
    ]


### Notes

-   Naive solution, to do it one by one.

    **Important**: 
    
    You go from the outside into the middle. So the main loop is half of the dimension. 
    
    The inner loop should also shrink its size everytime. Begins at i and ends and n-2-i, **not n-1-i**. 
    
    Because you don't want to swap the last one. The last one n-1-i has already been swapped with the i.

-   Another solution: how to rotate a matrix faster

    Swap the diagnoal elements and reverse each line in the matrix.
    
    <table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">
    
    
    <colgroup>
    <col  class="org-right" />
    
    <col  class="org-right" />
    
    <col  class="org-right" />
    
    <col  class="org-left" />
    
    <col  class="org-right" />
    
    <col  class="org-right" />
    
    <col  class="org-right" />
    
    <col  class="org-left" />
    
    <col  class="org-right" />
    
    <col  class="org-right" />
    
    <col  class="org-right" />
    </colgroup>
    <tbody>
    <tr>
    <td class="org-right">1</td>
    <td class="org-right">2</td>
    <td class="org-right">3</td>
    <td class="org-left">swap</td>
    <td class="org-right">1</td>
    <td class="org-right">4</td>
    <td class="org-right">7</td>
    <td class="org-left">reverse</td>
    <td class="org-right">7</td>
    <td class="org-right">4</td>
    <td class="org-right">1</td>
    </tr>
    
    
    <tr>
    <td class="org-right">4</td>
    <td class="org-right">5</td>
    <td class="org-right">6</td>
    <td class="org-left">&#x2014;></td>
    <td class="org-right">2</td>
    <td class="org-right">5</td>
    <td class="org-right">8</td>
    <td class="org-left">-&#x2013;&#x2014;></td>
    <td class="org-right">8</td>
    <td class="org-right">5</td>
    <td class="org-right">2</td>
    </tr>
    
    
    <tr>
    <td class="org-right">7</td>
    <td class="org-right">8</td>
    <td class="org-right">9</td>
    <td class="org-left">&#xa0;</td>
    <td class="org-right">3</td>
    <td class="org-right">6</td>
    <td class="org-right">9</td>
    <td class="org-left">&#xa0;</td>
    <td class="org-right">9</td>
    <td class="org-right">6</td>
    <td class="org-right">3</td>
    </tr>
    </tbody>
    </table>


### Solution

-   Solution 1: Straightforward

        class Solution(object):
            def rotate(self, matrix):
                """
                :type matrix: List[List[int]]
                :rtype: None Do not return anything, modify matrix in-place instead.
                """
                n = len(matrix)
        
                for i in range(n//2):
                    # Shrink the dimension
                    # Do not include the last element
                    for j in range(i, n-i-1):
                        tmp = matrix[i][j]
                        matrix[i][j] = matrix[n-1-j][i]
                        matrix[n-1-j][i] = matrix[n-1-i][n-1-j]
                        matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
                        matrix[j][n-1-i] = tmp
        
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        Solution().rotate(matrix)
        [print(*line) for line in matrix]

-   Solution 2:

        class Solution(object):
            def rotate(self, matrix):
                """
                :type matrix: List[List[int]]
                :rtype: None Do not return anything, modify matrix in-place instead.
                """
                n = len(matrix)
        
                for i in range(n):
                    for j in range(i, n):
                        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
                for i in range(n):
                    matrix[i].reverse()
        
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        Solution().rotate(matrix)
        [print(*line) for line in matrix]


<a id="org18f24d4"></a>

## 53 - Maximum Subarray

[leetcode](https://leetcode.com/problems/maximum-subarray/)


### Problem

    Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
    
    Example:
    
    Input: [-2,1,-3,4,-1,2,1,-5,4],
    Output: 6
    Explanation: [4,-1,2,1] has the largest sum = 6.
    Follow up:
    
    If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.


### Notes

Dynamic programming problem.

Use nums[i] always store the maximum sum.

maxSum(i) = maxSum(i-1) + nums[i] only if maxSum(i-1) > 0


### Solution

-   Solution 1: use a extra dp array

        class Solution(object):
            def maxSubArray(self, nums):
                """
                :type nums: List[int]
                :rtype: int
                """
                curSum = maxSum = nums[0]
        
                for num in nums[1:]:
                  curSum = max(num, curSum+num)
                  maxSum = max(curSum, maxSum)
        
                return maxSum
        
        print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

-   Solution 2: no extra space, in place modify

        class Solution(object):
            def maxSubArray(self, nums):
                """
                :type nums: List[int]
                :rtype: int
                """
        
                if len(nums) == 0:
                    return 0
        
                ret = nums[0]
        
                for i in range(1, len(nums)):
                    if nums[i - 1] > 0:
                        nums[i] += nums[i - 1]
        
                    ret = max(ret, nums[i])
        
                return ret
        print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))


<a id="orgce7eaa6"></a>

## 55 - Jump Game

[leetcode](https://leetcode.com/problems/jump-game/)


### Problem

    Given an array of non-negative integers, you are initially positioned at the first index of the array.
    
    Each element in the array represents your maximum jump length at that position.
    
    Determine if you are able to reach the last index.
    
    Example 1:
    
    Input: [2,3,1,1,4]
    Output: true
    Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
    
    Example 2:
    
    Input: [3,2,1,0,4]
    Output: false
    Explanation: You will always arrive at index 3 no matter what. Its maximum
                 jump length is 0, which makes it impossible to reach the last index.


### Notes

Greedy algorithm. There are 2 approaches, from head or from tail.

-   Start from head

    always remember the furthest reachable index.
    
        reach = max(i + nums[i], reach) if i <= reach

-   Start from tail

    always remember the last position it can reach.
    
        lastPos = i if i + nums[i] >= lastPos


### Solition

-   Solution 1: start from head

        class Solution():
            def canJump(self, nums):
                reach = 0
        
                for i in range(len(nums)):
                    if i <= reach:
                        reach = max(i + nums[i], reach)
        
                return reach >= len(nums) - 1
        
        print(Solution().canJump([ 2,3,1,1,4 ]))
        print(Solution().canJump([ 3,2,1,0,4 ] ))

-   Solution 2: start from tail

        class Solution():
            def canJump(self, nums):
                lastPos = len(nums) - 1
                for i in reversed(range(len(nums))):
                    if i + nums[i] >= lastPos:
                        lastPos = i
        
                return lastPos == 0
        
        print(Solution().canJump([ 2,3,1,1,4 ]))
        print(Solution().canJump([ 3,2,1,0,4 ] ))


<a id="orgfe08b35"></a>

## 62 - Unique Paths

[leetcode](https://leetcode.com/problems/unique-paths/)


### Problem

    A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
    
    The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
    
    How many possible unique paths are there?
    
    Note: m and n will be at most 100.
    
    Example 1:
    
    Input: m = 3, n = 2
    Output: 3
    Explanation:
    From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
    1. Right -> Right -> Down
    2. Right -> Down -> Right
    3. Down -> Right -> Right
    Example 2:
    
    Input: m = 7, n = 3
    Output: 28


### Notes

It is a DP problem. 

1.  There are only two possibilities to arrive at the finish point 
    1.  arrive at that point from above
    2.  arrive at that point from left

2.  So the ways to arrive at current point is equal to the ways from above plus the ways from left. dp[i][j] = dp[i][j-1] + dp[i - 1][j]
3.  Dynamic programming. Maintain a two dimensional matrix.
4.  Optimize it to one dimension.
5.  Complexity O(m \* n)

-   UniquePath with 2-D DP

        dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    After you have the edge, you go levelly to the bottom.

-   UniquePath with 1-D DP

        dp[j] = dp[j - 1] + dp[j]


### Solution

-   Solution 1: 2-D DP

        class Solution():
            def uniquePath(self, m, n):
                dp = [[1 for j in range(n)] for i in range(m)]
                for i in range(1, m):
                    for j in range(1, n):
                        dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
        
                return dp[-1][-1] if m and n else 0

-   Solution 2: 1-D DP

        class Solution():
            def uniquePath(self, m, n):
                dp = [1] * n
        
                for i in range(1, m):
                    for j in range(1, n):
                        dp[j] = dp[j - 1] + dp[j]
        
                return dp[-1] if m and n else 0


<a id="orgfe70ebe"></a>

## 64 - Minimum Path Sum

[leetcode](https://leetcode.com/problems/minimum-path-sum/)


### Problem

    Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
    
    Note: You can only move either down or right at any point in time.
    
    Example:
    
    Input:
    [
      [1,3,1],
      [1,5,1],
      [4,2,1]
    ]
    Output: 7
    Explanation: Because the path 1→3→1→1→1 minimizes the sum.


### Notes

Thinking: <del>It seems to be a greedy algorithm problem.</del>

It is a dp problem.

dp equation:

dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + grid[i][j]

Remember to handle the edge cases.


### Solution

-   Solution 1: 2D DP

    -   Inplace DP
    
        class Solution(object):
            def minPathSum(self, grid):
                """
                :type grid: List[List[int]]
                :rtype: int
                """
                m = len(grid)
                n = len(grid[0])
        
                for i in range(m):
                    for j in range(n):
                        if i == 0:
                            if j == 0:
                                continue
                            else:
                                grid[i][j] += grid[i][j-1]
                        else:
                            if j == 0:
                                grid[i][j] += grid[i-1][j]
                            else:
                                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
                return grid[-1][-1] if m and n else 0
        
        
        grid = [[1,3,1],[1,5,1],[4,2,1]]
        
        print(Solution().minPathSum(grid))
    
    -   Additional DP with auxiliary columns
    
        import sys
        class Solution(object):
            def minPathSum(self, grid):
                """
                :type grid: List[List[int]]
                :rtype: int
                """
                m = len(grid)
                n = len(grid[0])
        
                dp = [[ 0 for i in range(n+1)] for j in range(m+1)]
        
                for i in range(len(dp)):
                  dp[i][0] = sys.maxsize
        
                for i in range(len(dp[0])):
                    dp[0][i] = sys.maxsize
        
                dp[1][1] = grid[0][0]
        
                for i in range(1, m+1):
                    for j in range(1, n+1):
                        if i == 1 and j == 1: 
                            continue
                        else:
                            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i-1][j-1]
        
        
                return dp[-1][-1] if m and n else 0
        
        
        grid = [[1,3,1],[1,5,1],[4,2,1]]
        
        print(Solution().minPathSum(grid))

-   Solution 2: 1D DP

        import sys
        class Solution(object):
            def minPathSum(self, grid):
                """
                :type grid: List[List[int]]
                :rtype: int
                """
                m = len(grid)
                n = len(grid[0])
        
                dp = [sys.maxsize for i in range(n+1)]
                dp[1] = grid[0][0]
        
                for i in range(m):
                    for j in range(n):
                      if i == 1 and j == 1:
                          continue
                      else:
                        dp[j+1] = min(dp[j+1], dp[j]) + grid[i][j]
        
                return dp[-1] if m and n else 0
        
        
        grid = [[1,3,1],[1,5,1],[4,2,1]]
        
        print(Solution().minPathSum(grid))


<a id="org6b85062"></a>

## 70 - Climbing Stairs

[leetcode](https://leetcode.com/problems/climbing-stairs/)


### Problem

    You are climbing a stair case. It takes n steps to reach to the top.
    
    Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
    
    Note: Given n will be a positive integer.
    
    Example 1:
    
    Input: 2
    Output: 2
    Explanation: There are two ways to climb to the top.
    1. 1 step + 1 step
    2. 2 steps
    Example 2:
    
    Input: 3
    Output: 3
    Explanation: There are three ways to climb to the top.
    1. 1 step + 1 step + 1 step
    2. 1 step + 2 steps
    3. 2 steps + 1 step


### Notes

The distinct ways to take n stair cases:

1.  take one step at last, the distinct ways to take n-1 stair cases  -> f(n-1) ways
2.  take two steps at last, the distinct ways to take n-2 stair cases -> f(n-2) ways

So f(n) = f(n-1) + f(n-2)


### Solution

    class Solution():
        def climbStairs(self, n):
            if n < 2:
                return n
    
            dp = [0] * n
    
            dp[0] = 1
            dp[1] = 2
    
            for i in range(2, n):
                dp[i] = dp[i-1] + dp[i-2]
    
            return dp[-1]


<a id="org998a903"></a>

## 91 - Decode Ways

[leetcode](https://leetcode.com/problems/decode-ways)


### Problem

    A message containing letters from A-Z is being encoded to numbers using the following mapping:
    
    'A' -> 1
    'B' -> 2
    ...
    'Z' -> 26
    Given a non-empty string containing only digits, determine the total number of ways to decode it.
    
    Example 1:
    
    Input: "12"
    Output: 2
    Explanation: It could be decoded as "AB" (1 2) or "L" (12).
    Example 2:
    
    Input: "226"
    Output: 3
    Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).


### Notes

DP problem.

1.  Initialize dp array with dp[0] = 1 as padding, the rest of them are 0.
2.  Start from the first index of the string.
    1.  If dp[i] is in range 1 to 9, dp[i] = dp[i-1]. The ways of decode will not increase, if it is 0, it remains 0.
    2.  If dp[i] is in range 10 to 26, dp[i] += dp[i-1]. The ways of decode increase by one, if it is 00, it remains 0.

**Important**:

1.  Corner cases: "0" -> 0, "1002" -> 0
2.  Notice the padding


### Solution

    class Solution():
        def numsDecodings(self, s):
    
            if not s:
              return 0
    
            n = len(s)
    
            dp = [0] * (n + 1)
    
            dp[0] = 1
    
            for i in range(1, n+1):
    
                if s[i-1: i] != '0':
                    dp[i] = dp[i-1]
    
                if i != 1 and '10' <= s[i-2:i] <= '26':
                    dp[i] += dp[i-2]
    
            return dp[-1]


<a id="org3e9f584"></a>

## 509 - Fibonacci Number

[leetcode](https://leetcode.com/problems/fibonacci-number/)


### Problem

    The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
    
    F(0) = 0,   F(1) = 1
    F(N) = F(N - 1) + F(N - 2), for N > 1.
    Given N, calculate F(N).
    
     
    
    Example 1:
    
    Input: 2
    Output: 1
    Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
    Example 2:
    
    Input: 3
    Output: 2
    Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
    Example 3:
    
    Input: 4
    Output: 3
    Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.


### Notes

DP Problem.

**Important**:

Note how long is the dp array. It shoud be N+1, since we start with the number 0.


### Solution

    class Solution(object):
        def fib(self, N):
            """
            :type N: int
            :rtype: int
            """
            if N < 2:
                return N
    
            dp = [0] * (N + 1)
    
            dp[0] = 0
            dp[1] = 1
    
            for i in range(2, N + 1):
                dp[i] = dp[i - 1] + dp[i - 2]
    
            return dp[-1]


<a id="orgb4b62c9"></a>

## 75 - Sort Colors

[leetcode](https://leetcode.com/problems/sort-colors/)


### Problem

    Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.
    
    Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
    
    Note: You are not suppose to use the library's sort function for this problem.
    
    Example:
    
    Input: [2,0,2,1,1,0]
    Output: [0,0,1,1,2,2]
    Follow up:
    
    A rather straight forward solution is a two-pass algorithm using counting sort.
    First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
    Could you come up with a one-pass algorithm using only constant space?


### Notes

-   First attempt is to use two pointer.

    There is a but a corner case: when two pointer are both at 1. How should we move the pointer.
    
    We can use a another `while` unter this situation, initialize another pointer and search for 0 or 2 between
    these two pointers. See Soution 1

-   Three Way Partition

    three pointer, one for each. 
    
    **Important**:
    
    Notice the condition for `while`: while mi <= hi
    
    the middle move forward:
    
    1.  middle == 0, switch with left one, left + 1, middle + 1
    2.  middle == 1, continue
    3.  middle == 2, swtich with right one, right - 1


### Solution

-   Solution 1

        class Solution(object):
            def sortColors(self, nums):
                """
                :type nums: List[int]
                :rtype: None Do not return anything, modify nums in-place instead.
                """
        
                lo = 0
                hi = len(nums) - 1
        
                while (lo < hi):
                    if nums[lo] == 0:
                        lo += 1
                    elif nums[hi] == 2:
                        hi -= 1
                    elif nums[lo] == 1 and nums[hi] == 1:
                        mi = lo + 1
                        while (mi < hi):
                            if nums[mi] == 2 or nums[mi] == 0:
                                nums[mi], nums[hi] = nums[hi], nums[mi]
                                break
                            else:
                                mi += 1
                        if mi == hi:
                            return
                    else:
                        nums[lo], nums[hi] = nums[hi], nums[lo]

-   Solution 2: Three way partition

    Notice the condition for `while`:
    
    It has to be <=. 
    Because you every element behind hi, you have seen it. 
    But not the element at hi. You have to check it at last.
    
        class Solution(object):
            def sortColors(self, nums):
        
                lo, mi, hi = 0, 0, len(nums) - 1
        
                while mi <= hi: # Nottice!: here has to be <=
                    if nums[mi] == 0:
                        nums[mi], nums[lo] = nums[lo], nums[mi]
                        lo += 1
                        mi += 1
                    elif nums[mi] == 2:
                        nums[mi], nums[hi] = nums[hi], nums[mi]
                        hi -= 1
                    else:
                        mi += 1


<a id="orgb2fdd47"></a>

## 78 - Subsets


### Problem

[leetcode](https://leetcode.com/problems/subsets/)

    Given a set of distinct integers, nums, return all possible subsets (the power set).
    
    Note: The solution set must not contain duplicate subsets.
    
    Example:
    
    Input: nums = [1,2,3]
    Output:
    [
      [3],
      [1],
      [2],
      [1,2,3],
      [1,3],
      [2,3],
      [1,2],
      []
    ]


### Notes

Three strategies to solve a subset problem:

Recursion, Backtracking, Bitmask

-   Recursion

    Iterative version:
    
        Start from empty array [[]].
        
        Step 1: Take 1 into consideration, and add 1 to existing array [[], [1]]
        
        Step 2: Take 2 into consideration, and add 2 to existing array [[], [1], [2], [1, 2]]
        
        Step 3: Take 3 into consideration, and add 3 to existing array [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    
    DFS version:
    
        [[]]
        [[], [1]],
        [[], [1], [1, 2]]
        [[], [1], [1, 2], [1, 2, 3]]
        [[], [1], [1, 2], [1, 2, 3], [1, 3]]
        [[], [1], [1, 2], [1, 2, 3], [1, 3], [2]]
        [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3]]
        [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]

-   Backtrack

    Backtrack needs to know how many steps it shoud take to end.
    
        [1, 2, 3]
        
        Step 1: subsets of length 0: [[]]
        Step 2: subsets of length 1: [[1], [2], [3]]
        Step 3: subsets of length 2: [[1, 2], [2, 3], [1, 3]]
        Step 4: subsets of length 3: [[1, 2, 3]]

-   Bitmask

    > The idea is that we map each subset to a bitmask of length n, 
    > where 1 on the ith position in bitmask means the presence of nums[i] in the subset, 
    > and 0 means its absence.
    
    [1, 2, 3]
    
        [0, 0, 0] -> []
        [0, 0, 1] -> [3]
        [0, 1, 0] -> [2]
        [1, 0, 0] -> [1]
        [1, 0, 1] -> [1, 3]
        [0, 1, 1] -> [2, 3]
        [1, 1, 0] -> [1, 2]
        [1, 1, 1] -> [1, 2, 3]


### Solution

-   Solution 1: dfs (recursion)

        class Solution(object):
            def subsets(self, nums):
                res = []
                self.dfs(sorted(nums), 0, [], res)
                return res
        
            def dfs(self, nums, index, path, res):
                res.append(path)
                for i in range(index, len(nums)):
                    self.dfs(nums, i + 1, path + [nums[i]], res)
        
        print(Solution().subsets([1, 2, 3]))

-   Solution 2: iterative

        class Solution:
        
            def subsets(self, nums):
                res = [[]]
                for i in sorted(nums):
                    res += [item+[i] for item in res]
        
                return res
        
        print(Solution().subsets([1, 2, 3]))

-   Solution 3: backtrack

        
        class Solution(object):
        
            def subsets(self, nums):
                output = []
                for k in range(0, len(nums)+1):
                    temp = []
                    self.backtrack(0, k, nums, temp, output)
        
                return output
        
            def backtrack(self, begin, length, nums, temp, output):
        
                if length == len(temp):
                    output.append(temp[:])
        
                for i in range(begin, len(nums)):
                    temp.append(nums[i])
                    self.backtrack(i+1, length, nums, temp, output)
                    temp.pop()
        
        
        print(Solution().subsets([1, 2, 3]))

-   Solution 4: bitmask

        
        class Solution():
          def subsets(self, nums):
            n = len(nums)
            output = []
            for i in range(2**n, 2**(n+1)):
              bitmask = bin(i)[3:]
              output.append([nums[i] for i in range(n) if bitmask[i] == '1' ])
        
            return output


<a id="orgade3b8e"></a>

## 79 - Word Search

[leetcode](https://leetcode.com/problems/word-search/)


### Problem

    Given a 2D board and a word, find if the word exists in the grid.
    
    The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
    
    Example:
    
    board =
    [
      ['A','B','C','E'],
      ['S','F','C','S'],
      ['A','D','E','E']
    ]
    
    Given word = "ABCCED", return true.
    Given word = "SEE", return true.
    Given word = "ABCB", return false.


### Notes

Backtrack problem. 

1.  when found, mark the point to one.
2.  Use dfs to go down from this point.
3.  Can't go down anymore, mark the point back to zero (backtrack step).


### Solution

-   Solution 1: Backtrack, dfs

        class Solution:
            def exist(self, board, word):
                m = [[0 for j in range(len(board[0]))] for i in range(len(board))]
                for i in range(len(board)):
                    for j in range(len(board[0])):
                        if self.exist_rec(board, word, i, j, m):
                            return True
                return False
        
            def exist_rec(self, board, word, i, j, m):
                if len(word) == 0:
                    return True
        
                if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
                    return False
        
                if board[i][j] == word[0] and m[i][j] == 0:
                    m[i][j] = 1
        
                    if self.exist_rec(board, word[1:], i - 1, j, m) or \
                    self.exist_rec(board, word[1:], i + 1, j, m) or \
                    self.exist_rec(board, word[1:], i, j - 1, m) or \
                    self.exist_rec(board, word[1:], i, j + 1, m):
                        return True
                    else:
                        m[i][j] = 0
        
                return False
        
        board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
        word = "ABCCED"


<a id="org177a595"></a>

## 45 - Jump Game II

[leetcode](https://leetcode.com/problems/jump-game-ii/)


### Problem

    Given an array of non-negative integers, you are initially positioned at the first index of the array.
    
    Each element in the array represents your maximum jump length at that position.
    
    Your goal is to reach the last index in the minimum number of jumps.
    
    Example:
    
    Input: [2,3,1,1,4]
    Output: 2
    Explanation: The minimum number of jumps to reach the last index is 2.
        Jump 1 step from index 0 to 1, then 3 steps to the last index.
    Note:
    
    You can assume that you can always reach the last index.


### Notes

Greedy problem.

1.  [begin, end], go through values in between, have one furthest reach.
2.  current index reach to end, jump once.
3.  next interval is [end, reach]


### Solution

    class Solution:
        def jump(self, nums):
    
            jumps = 0
            curFurthest = 0
            curEnd = 0
    
            for i in range(len(nums) - 1):
    
                curFurthest = max(curFurthest, i + nums[i])
    
                if (i == curEnd):
                    jumps += 1
                    curEnd = curFurthest
    
            return jumps


<a id="org4b122a4"></a>

## 1306 - Jump Game III

[leetcode](https://leetcode.com/problems/jump-game-iii/submissions/)


### Problem

    Given an array of non-negative integers arr, you are initially positioned at start index of the array. When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach to any index with value 0.
    
    Notice that you can not jump outside of the array at any time.
    
    Example 1:
    
    Input: arr = [4,2,3,0,3,1,2], start = 5
    Output: true
    Explanation: 
    All possible ways to reach at index 3 with value 0 are: 
    index 5 -> index 4 -> index 1 -> index 3 
    index 5 -> index 6 -> index 4 -> index 1 -> index 3 
    
    Example 2:
    
    Input: arr = [4,2,3,0,3,1,2], start = 0
    Output: true 
    Explanation: 
    One possible way to reach at index 3 with value 0 is: 
    index 0 -> index 4 -> index 1 -> index 3
    
    Example 3:
    
    Input: arr = [3,0,2,1,2], start = 2
    Output: false
    Explanation: There is no way to reach at index 1 with value 0.
    
    Constraints:
    
    1 <= arr.length <= 5 * 10^4
    0 <= arr[i] < arr.length
    0 <= start < arr.length


### Notes

Use dfs to search for 0. Mark the visited place to trigger stop.

**Important**:

Remember to reset the mark if can not find along the path, so that it can search into another path.


### Solution

    class Solution:
        def canReach(self, arr, start):
            if start >= len(arr) or start < 0:
                return False
    
            if arr[start] == 0:
                return True
    
            if arr[start] == -1:
                return False
    
            step = arr[start]
            arr[start] = -1
    
            if self.canReach(arr, start - step) or self.canReach(arr, start + step):
                return True
            else:
                arr[start] = step
                return False


<a id="org3cfebe9"></a>

## 84 - Largest Rectangle in Histogram

[leetcode](https://leetcode.com/problems/largest-rectangle-in-histogram/)


### Problem

    Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.
    
    Example:
    
    Input: [2,1,5,6,2,3]
    Output: 10

![img](Algorithms/2020-03-23_00-34-37_histogram.png)
Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

![img](Algorithms/2020-03-23_00-35-27_histogram_area.png)
The largest rectangle is shown in the shaded area, which has area = 10 unit.


### Notes

Main idea is to caculate both left edge and right edge for every entry in the array

Two ways of solution.

-   Brute Force

    Generate two arrays left[] and right[] to keep the two edges of every entry.
    
    1.  one loop to caculate left[].
    2.  one loop to caculate right[].
    3.  one loop to go through all the edges to caculate the square.

-   Improvement of the brute force

    We can:
    
    store the number of the left bars, which are >= current bar, in left[]
    
    store the number of the right bars, which are >= current bar, in right[]
    
    How to avoid duplicating searching.
    
    1.  left[current] = left[current - 1]
    2.  jump left[current - 1] steps to check the next interval of the array

-   Stack

    Create a stack to store the index of the entry.
    
    1.  if current entry is smaller than the top, we find the right edge of the top entry. pop it out and caculate the the max square of the top entry
    2.  if current entry is not smaller than the top, push it into stack
    3.  go through the left entries in the stack. The lefts ones are all have the longest bar at the top.


### Solution

-   Solution 1: brute-force

        class Solution:
            def largestRectangleArea(self, heights):
        
                if not heights:
                    return 0
        
                n = len(heights)
                res = 0
        
                left = [ i for i in range(n) ]
                right = [ i for i in range(n) ]
        
                # caculate for the left edge
                for i in range(n):
                    p = i
                    while p >= 0:
                        if heights[p] < heights[i]:
                            break
                        p -= 1
                    left[i] = p
        
                # caculate for the right edge
                for i in range(n):
                    p = i
                    while p < n:
                        if heights[p] < heights[i]:
                            break
                        p += 1
                    right[i] = p
        
                for i in range(n):
                    res = max(res, heights[i] * (right[i] - left[i] - 1))
        
                return res
        
        print(Solution().largestRectangleArea([2, 1, 5, 6, 2, 3]))
    
    O(n^2)
    
    It will execeed time limit on leetcode.
    
        10

-   Solution 2: improved version

        class Solution:
            def largestRectangleArea(self, heights):
                if not heights:
                    return 0
        
                res = 0
                n = len(heights)
                left = [1] * n
                right = [1] * n
        
                # caculate left[]
                for i in range(n):
                    p = i - 1
                    while p >= 0:
                        if heights[p] >= heights[i]:
                            left[i] += left[p]
                            # jump backward
                            p -= left[p]
                        else:
                            break
        
                # caculate right[]
                for i in range(n - 1, -1, -1):
                    p = i + 1
                    while p < n:
                        if heights[p] >= heights[i]:
                            right[i] += right[p]
                            # jump forward
                            p += right[p]
                        else:
                            break
        
                for i in range(n):
                    res = max(res, heights[i] * (left[i] + right[i] - 1))
        
                return res
        
        print(Solution().largestRectangleArea([2, 1, 5, 6, 2, 3]))
    
    Generale Case: O(n), because it uses the jump
    Worst Case: O(n^2)

-   Solution 3: stack

        class Solution:
            def largestRectangleArea(self, heights):
        
                stack = []
                n = len(heights)
                res = 0
                index = 0
        
                while index < n:
        
                    if not stack or heights[stack[-1]] <= heights[index]:
                        stack.append(index)
                        index += 1
                    else:
                        top = stack.pop()
                        area = (heights[top] *
                                ((index - stack[-1] - 1) if stack else index))
        
                        res = max(res, area)
        
                while stack:
                    h = stack.pop()
                    res = max(
                        res,
                        heights[h] * ((n - stack[-1] - 1) if stack else n))
        
                return res
        
        
        print(Solution().largestRectangleArea([2, 1, 5, 6, 2, 3]))


<a id="org23ce5eb"></a>

## 85 - Maximal Rectangle

[leetcode](https://leetcode.com/problems/maximal-rectangle/)


### Problem

    Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.
    
    Example:
    
    Input:
    [
      ["1","0","1","0","0"],
      ["1","0","1","1","1"],
      ["1","1","1","1","1"],
      ["1","0","0","1","0"]
    ]
    Output: 6


### Notes

Two parts:

1.  generate a heights histogram for every row.
2.  apple "largest rectangle in histogram" on each row of histogram


### Solution

    class Solution:
        def maximalRectangle(self, matrix):
            if not matrix or not matrix[0]:
                return 0
    
            m = len(matrix)
            n = len(matrix[0])
    
            histograms = [[0] * n for i in range(m)]
    
            res = 0
    
            for i in range(m):
                for j in range(n):
                    if matrix[i][j] == "1":
                        histograms[i][j] = histograms[i - 1][j] + 1 if i > 0 else 1
    
            for histogram in histograms:
                res = max(res, self.largestRectangleHistogram(histogram))
    
            return res
    
        def largestRectangleHistogram(self, histogram):
    
            if not histogram:
                return 0
    
            stack = []
            res = 0
            index = 0
            n = len(histogram)
    
            while index < n:
                if not stack or histogram[index] >= histogram[stack[-1]]:
                    stack.append(index)
                    index += 1
                else:
                    res = max(
                        res, histogram[stack.pop()] *
                        ((index - stack[-1] - 1) if stack else index))
    
            while stack:
                height = histogram[stack.pop()]
                res = max(res, height * ((n - stack[-1] - 1) if stack else n))
    
            return res
    
    maxtrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    
    print(Solution().maximalRectangle(maxtrix))


<a id="org8faa9e8"></a>

## 121 - Best Time to Buy and Sell Stock

[leetcode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)


### Problem

    Say you have an array for which the ith element is the price of a given stock on day i.
    
    If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
    
    Note that you cannot sell a stock before you buy one.
    
    Example 1:
    
    Input: [7,1,5,3,6,4]
    Output: 5
    Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
                 Not 7-1 = 6, as selling price needs to be larger than buying price.
                 
    Example 2:
    
    Input: [7,6,4,3,1]
    Output: 0
    Explanation: In this case, no transaction is done, i.e. max profit = 0.


### Notes

Mark the minPrice and the minProfit


### Solution

    class Solution:
        def maxProfit(self, prices):
            if not prices:
                return 0
    
            minPrice = prices[0]
            maxProfit = 0
    
            for price in prices:
                if price < minPrice:
                    minPrice = price
                if price - minPrice > maxProfit:
                    maxProfit = price - minPrice
            return maxProfit


<a id="orga0f7a9f"></a>

## 122 - Best Time to Buy and Sell Stock II

[leetcode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii)


### Problem

    Say you have an array for which the ith element is the price of a given stock on day i.
    
    Design an algorithm to find the maximum profit. You may complete as many transactions as you like
    
    Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
    
    Example 1:
    
    Input: [7,1,5,3,6,4]
    Output: 7
    Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
                 Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
    Example 2:
    
    Input: [1,2,3,4,5]
    Output: 4
    Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
                 Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
                 engaging multiple transactions at the same time. You must sell before buying again.
    Example 3:
    
    Input: [7,6,4,3,1]
    Output: 0
    Explanation: In this case, no transaction is done, i.e. max profit = 0.


### Notes

-   Solution 1

    Find the valley and peak, save the local maxProfit, add it up when new valley is found.

-   Solution 2

    Simplify the solution 1:
    we can sum up the profit when we go up step by step. 


### Solution

-   Solution 1:

        class Solution:
            def maxProfit(self, prices):
                if not prices:
                    return 0
        
                valley = prices[0]
                maxProfit = 0
                res = 0
        
                for price in prices:
                    if price - valley < maxProfit:
                        valley = price # new valley
                        res += maxProfit # add the current maxProfit
                        maxProfit = 0 # reset current maxProfit
                    else:
                        maxProfit = price - valley # update the maxProfit when we still go up
        
                # remember to add the last maxProfit.
                # 1. When we are on the peak. maxProfit > 0, it should be added
                # 2. When we are in the vally, maxProfit = 0, would not affect the value
                res += maxProfit
        
                return res

-   Solution 2:

        class Solution:
            def maxProfit(self, prices):
                res = 0
                for i in range(1, len(prices)):
                    if (prices[i-1] < prices[i]):
                        res += prices[i] - prices[i-1]
                return res


<a id="org6d99ebf"></a>

## 123 - Best Time to Buy and Sell Stock III

[leetcode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/)


### Problem

    Say you have an array for which the ith element is the price of a given stock on day i.
    
    Design an algorithm to find the maximum profit. You may complete at most two transactions.
    
    Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
    
    Example 1:
    
    Input: [3,3,5,0,0,3,1,4]
    Output: 6
    Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
                 Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
    Example 2:
    
    Input: [1,2,3,4,5]
    Output: 4
    Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
                 Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
                 engaging multiple transactions at the same time. You must sell before buying again.
    Example 3:
    
    Input: [7,6,4,3,1]
    Output: 0
    Explanation: In this case, no transaction is done, i.e. max profit = 0.


### Notes

A very good article about how to solve this kind of problem generally. [[Reference]​](https://labuladong.gitbook.io/algo/dong-tai-gui-hua-xi-lie/tuan-mie-gu-piao-wen-ti)

DP problem have three main sub problems:

1.  states => DP-Table
2.  states transition => Transition
3.  base cases => Padding or Initializtion

DP is also some kind of brute force method. We have to find all the states of the problem.
And we try to use the sub-states to apply the state transitions to simplify the calculation.

How many states do we have in all:

1.  number of days, n
2.  numebr of transactions, k = 2
3.  have the stock or not, 0 or 1

state[n][k][0 or 1] means:

the state at the n-th day, already k times transactions, have or have not the stock in hand.

State Transition:

1.  state[n][k][0] = max(state[n-1][k][0], state[n-1][k][1] + prices)
    
    state: I have no stock in hand
    
    It can transit from two states:
    
    -   I do not have stock yesterday               => state[n-1][k][0]
    
    -   I do have stock yesterday, and I sell it    => state[n-1][k][1] + prices

2.  state[n][k][1] = max(state[n-1][k][1], state[n-1][k-1][0] - prices)
    
    state: I have stock in hand
    
    It can transit from two states:
    
    -   I do have stock yesterday                   => state[n-1][k][1]
    
    -   I don't have stock yesterday, and I buy it  => state[n-1][k-1][1] - prices


### Solution

    class Solution:
        def maxProfit(self, prices):
            max_k = 2
            dp = [ [ [0] * 2 for k in range(max_k + 1) ] for i in range(len(prices))]
            for i in range(len(prices)):
                for k in range(1, max_k + 1):
                    if i == 0:
                        dp[i][k][0] = 0
                        dp[i][k][1] = -prices[i]
                    else:
                        dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
                        dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
    
            return dp[-1][max_k][0]

Simple Version: reduce the DP-Table

We only have to maintain two 1-dimentional states.

    import sys
    class Solution:
        def maxProfit(self, prices):
            buy = [-sys.maxsize] * 3
            sell = [0] * 3
            for price in prices:
                buy[1] = max(buy[1], sell[0]-price)
                buy[2] = max(buy[2], sell[1]-price)
                sell[1] = max(sell[1], buy[1]+price)
                sell[2] = max(sell[2], buy[2]+price)
                print(buy)
                print(sell)
            return sell[2]
    
    print(Solution().maxProfit([3,3,5,0,0,3,1,4]))


<a id="org895dda4"></a>

## 188 - Best Time to Buy and Sell Stock IV

[leetcode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/)


### Problem

    Say you have an array for which the i-th element is the price of a given stock on day i.
    
    Design an algorithm to find the maximum profit. You may complete at most k transactions.
    
    Note:
    You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
    
    Example 1:
    
    Input: [2,4,1], k = 2
    Output: 2
    Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
    
    Example 2:
    
    Input: [3,2,6,5,0,3], k = 2
    Output: 7
    Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4.
                 Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.


### Notes

See problem 121, 122 and 123.

Note the k.
If it is too large(>= n/2), treat it as if with infinitive transactions. We don't want to loop through a too large k.


### Solution

    class Solution:
        def maxProfit(self, k, prices):
            if not prices:
                return 0
    
            n = len(prices)
            if k >= n//2: # treat it as infinitive transactions
                res = 0
                for i in range(1, n):
                    if prices[i] > prices[i-1]:
                        res += prices[i] - prices[i-1]
                return res
    
            buy = [-sys.maxsize] * (k+1)
            sell = [0] * (k+1)
    
            for price in prices:
                for i in range(1, k+1):
                    buy[i] = max(buy[i], sell[i-1]-price)
                    sell[i] = max(sell[i], buy[i]+price)
    
    
            return sell[-1]


<a id="orge52e1b3"></a>

## 309 - Best Time to Buy and Sell Stock with Cooldown

[leetcode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown)


### Problem

    Say you have an array for which the ith element is the price of a given stock on day i.
    
    Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:
    
    You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
    After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
    Example:
    
    Input: [1,2,3,0,2]
    Output: 3 
    Explanation: transactions = [buy, sell, cooldown, buy, sell]


### Notes


### Solution

    import sys
    class Solution:
        def maxProfit(self, prices):
            dp_buy = -sys.maxsize
            dp_sell = 0
            dp_pre_0 = 0
    
            for price in prices:
                tmp = dp_sell
                dp_sell = max(dp_sell, dp_buy + price)
                dp_buy = max(dp_buy, dp_pre_0 - price)
                dp_pre_0 = tmp
    
            return dp_sell


<a id="org27b3f8c"></a>

## 104 - Maximum Depth of Binary Tree

[leetcode](https://leetcode.com/problems/maximum-depth-of-binary-tree/)


### Problem

    Given a binary tree, find its maximum depth.
    
    The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
    
    Note: A leaf is a node with no children.
    
    Example:
    
    Given binary tree [3,9,20,null,null,15,7],
    
        3
       / \
      9  20
        /  \
       15   7


### Notes

Recursion is your friend!


### Solution

    class Solution:
        def maxDepth(self, root):
            return 1 + max(self.maxDepth(root.right), self.maxDepth(root.left)) if root else 0


<a id="org967a7f4"></a>

## 21 - Merge Two Sorted Lists

[leetcode](https://leetcode.com/problems/merge-two-sorted-lists/)


### Problem

    Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
    
    Example:
    
    Input: 1->2->4, 1->3->4
    Output: 1->1->2->3->4->4


### Notes

Recursion is your friend!


### Solution

-   Solution 1: Recursive

        class Solution:
            def mergeTwoLists(self, l1, l2):
                if not l1:
                    return l2
                if not l2:
                    return l1
        
                if l1.val > l2.val:
                    l2.next = self.mergeTwoLists(l1, l2.next)
                    return l2
                else:
                    l1.next = self.mergeTwoLists(l1.next, l2)
                    return l1

-   TODO Solution 2: How to do it none recursively


<a id="org00dd672"></a>

## 101 - Symmetric Tree

[leetcode](https://leetcode.com/problems/symmetric-tree/)


### Problem

    Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
    
    For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
    
        1
       / \
      2   2
     / \ / \
    3  4 4  3
     
    
    But the following [1,2,2,null,3,null,3] is not:
    
        1
       / \
      2   2
       \   \
       3    3


### Notes

Recursion !


### Solution

-   Solution 1: recursive

        class Solution:
            def isSymmetric(self, root):
                if not root:
                    return True
                return self.isMirrored(root.left, root.right)
        
            def isMirrored(self, left, right):
        
                if not left and not right:
                    return True
                elif not left:
                    return False
                elif not right:
                    return False
                else:
                    if left.val == right.val:
                        return self.isMirrored(left.left, right.right) and \
                            self.isMirrored(left.right, right.left)
                    else:
                        return False

-   TODO Solution 2: How to solve it non recursively


<a id="orgc3e81fc"></a>

## 198 - House Robber

[leetcode](https://leetcode.com/problems/house-robber/)


### Problem

    You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
    
    Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
    
    Example 1:
    
    Input: [1,2,3,1]
    Output: 4
    Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
                 Total amount you can rob = 1 + 3 = 4.
    Example 2:
    
    Input: [2,7,9,3,1]
    Output: 12
    Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
                 Total amount you can rob = 2 + 9 + 1 = 12.


### Notes

States: 1. house, 2. rob or not rob -> dp[i][0 or 1]

Transition: dp[i][0] = max(dp[i-1][0], dp[i-1][1]), dp[i][1] = dp[i-1][0] + nums[i]

Base Case: dp[0][0] = 0, dp[0][1] = 0


### Solution

    class Solution:
        def rob(self, nums):
            robbed, notRobbed = 0, 0
            for i in nums:
                robbed, notRobbed = notRobbed + i, max(robbed, notRobbed)
            return max(robbed, notRobbed)


<a id="org74ed72b"></a>

## 300 - Longest Increasing Subsequence

[leetcode](https://leetcode.com/problems/longest-increasing-subsequence/)


### Problem

    Given an unsorted array of integers, find the length of longest increasing subsequence.
    
    Example:
    
    Input: [10,9,2,5,3,7,101,18]
    Output: 4 
    Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
    Note:
    
    There may be more than one LIS combination, it is only necessary for you to return the length.
    Your algorithm should run in O(n2) complexity.
    Follow up: Could you improve it to O(n log n) time complexity?


### Notes

-   Solution 1: DP with O(n^2)

    DP problem
    
    States: index, dp[index] = longest increasing subsequence at this position
    
    Transition: if nums[j] < nums[i]: dp[i] = max(dp[i], dp[j] + 1) 
    
    Base Case: dp[0] = 1

-   Solution 2: DP with binary search


### Solution

-   Solution 1: DP with O(n^2)

        class Solution:
            def lengthOfLIS(self, nums):
                dp = [1] * len(nums)
        
                for i in range(1, len(nums)):
                    for j in range(i):
                        if nums[j] < nums[i]:
                            dp[i] = max(dp[i], dp[j] + 1)
        
                return max(dp) if nums else 0

-   TODO Solution 2: DP with binary search


<a id="org3e33279"></a>

## 322 - Coin Change

[leetcode](https://leetcode.com/problems/coin-change/)


### Problem

    You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
    
    Example 1:
    
    Input: coins = [1, 2, 5], amount = 11
    Output: 3 
    Explanation: 11 = 5 + 5 + 1
    Example 2:
    
    Input: coins = [2], amount = 3
    Output: -1
    
    Note:
    You may assume that you have an infinite number of each kind of coin.


### Notes

DP problem

States: amount

Transition: dp[i] = min(dp[i], dp[i-coins[j]]+1)


### Solution

    class Solution:
        def coinChange(self, coins, amount):
            dp = [float('inf')] * (amount + 1)
    
            dp[0] = 0
    
            for i in range(1, amount + 1):
                for j in range(len(coins)):
                    if i - coins[j] >= 0:
                        dp[i] = min(dp[i], dp[i - coins[j]] + 1)
    
            return dp[-1] if dp[-1] != float('inf') else -1

