
# LeetCode <code>[41/42]</code>


# Table of Contents

-   [LeetCode <code>[41/42]</code>](#org5bf5bd5)
    -   [41 - First Missing Positive](#orgc43c0b6)
    -   [48 - Rotate Image](#org6757f65)
    -   [53 - Maximum Subarray](#orge4c55c5)
    -   [55 - Jump Game](#orga006a2d)
    -   [62 - Unique Paths](#orgee32675)
    -   [64 - Minimum Path Sum](#org69e2610)
    -   [70 - Climbing Stairs](#org18a7373)
    -   [91 - Decode Ways](#orge944c55)
    -   [509 - Fibonacci Number](#orga249e82)
    -   [75 - Sort Colors](#org2aa21ca)
    -   [79 - Word Search](#orgf51bd83)
    -   [45 - Jump  ame II](#org561d722)
    -   [1306 - Jump Game III](#org21905eb)
    -   [84 - Largest Rectangle in Histogram](#org32938a4)
    -   [85 - Maximal Rectangle](#org8934f21)
    -   [121 - Best Time to Buy and Sell Stock](#org9721637)
    -   [122 - Best Time to Buy and Sell Stock II](#org9e8b9fe)
    -   [123 - Best Time to Buy and Sell Stock III](#orgec1d701)
    -   [188 - Best Time to Buy and Sell Stock IV](#org93f588b)
    -   [309 - Best Time to Buy and Sell Stock with Cooldown](#org61b699b)
    -   [104 - Maximum Depth of Binary Tree](#org06a2063)
    -   [21 - Merge Two Sorted Lists](#orgfb8573b)
    -   [101 - Symmetric Tree](#org43d5a31)
    -   [198 - House Robber](#orgb89894b)
    -   [300 - Longest Increasing Subsequence](#org47da147)
    -   [322 - Coin Change](#org1d673dd)
    -   [152 - Maximum Product Subarray](#org8e1d843)
    -   [96 - Unique Binary Search Trees](#org8ea3ee2)
    -   [221 - Maximal Square](#org08f31e1)
    -   [279 - Perfect Squares](#orgc00f091)
    -   [647 - Palindromic Substrings](#org1a92df8)
    -   [5 - Longest Palindromic Substring](#org5e53d5f)
    -   [136 - Single Number](#org3b14b89)
    -   [202 - Happy Number](#org92fa83a)
    -   [338 - Counting Bits](#org57e27bb)
    -   [494 - Target Sum](#orgd9bf15b)
    -   [283 - Move Zeros](#org8d901a7)
    -   [416 - Partition Equal Subset Sum](#org41cd874)
    -   [698 - Partition to K Equal Sum Subsets](#orgf324966)
    -   [215 - Kth Largest Element in an Array](#org65c395e)
    -   [49 - Group Anagrams](#org19f1873)
    -   [876 - Middle of the Linked List](#org6c8b5aa)


<a id="orgc43c0b6"></a>

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


<a id="org6757f65"></a>

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


<a id="orge4c55c5"></a>

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


<a id="orga006a2d"></a>

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


<a id="orgee32675"></a>

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


<a id="org69e2610"></a>

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


<a id="org18a7373"></a>

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


<a id="orge944c55"></a>

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


<a id="orga249e82"></a>

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


<a id="org2aa21ca"></a>

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

    There is a but a corner case: when two point+begin\_src python :results output 
      class Solution:
    
    def subsets(self, nums):
        res = [[]]
        for i in sorted(nums):
            res <del>= [item</del>[i] for item in res]
    
    return res
    
      print(Solution().subsets([1, 2, 3]))
    \#+end\_src
    
        [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

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


<a id="orgf51bd83"></a>

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


<a id="org561d722"></a>

## 45 - Jump  ame II

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

\#+begin\_src python 
  class Solution:
      def jump(self, nums):

jumps = 0
curFurthest = 0
curEnd = 0

for i in range(len(nums) - 1):

curFurthest = max(curFurthest, i + nums[i])

if (i `= curEnd):
                  jumps +` 1
    cur


<a id="org21905eb"></a>

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

\#+begin\_src python  
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


<a id="org32938a4"></a>

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

    \#+begin\_src python :results output
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
        area = (heights[top] \*
                ((index - stack[-1] - 1) if stack else index))
    
    res = max(res, area)
    
    while stack:
        h = stack.pop()
        res = max(
            r


<a id="org8934f21"></a>

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

\#+begin\_src python :results output
  class Solution:
      def maximalRectangle(self, matrix):
          if not matrix or not matrix[0]:
              return 0

m = len(matrix)
n = len(matrix[0])

histograms = [[0] \* n for i in range(m)]

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
            res, histogram[stack.pop()] \*
            ((index - stack[-1] - 1) if stack else index))

while stack:
    height = histogram[stack.pop()]
    res = max(res, height \* ((n - stack[-1] - 1) if stack else n))

return res

maxtrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0",


<a id="org9721637"></a>

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

\#+begin\_src python  
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
        maxProfit = price 


<a id="org9e8b9fe"></a>

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

    \#+begin\_src python  
      class Solution:
          def maxProfit(self, prices):
              res = 0
              for i in range(1, len(prices)):
                  if (prices[i-1] < prices[i]):


<a id="orgec1d701"></a>

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
3.  base cases => Padding or initializtion

DP is also a form of brute force method. We have to find all the states of the problem.
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
    
    -   I do have stock yesterday, and I sell it    => state[n-1][k][1] + price

2.  state[n][k][1] = max(state[n-1][k][1], state[n-1][k-1][0] - prices)
    
    state: I have stock in hand
    
    It can transit from two states:
    
    -   I do have stock yesterday                   => state[n-1][k][1]
    
    -   I don't have stock yesterday, and I buy it  => state[n-1][k-1][1] - price


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

\#+begin\_example
[-9223372036854775807, -3, -3]
[0, 0, 0]
[-9223372036854775807, -3, -3]
[0, 0, 0]
[-9223372036854775807, -3, -3]
[0, 2, 2]
[-9223372036854775807, 0, 2]
[0, 2, 2]
[-9223372036854775807, 0, 2]
[0, 2, 2]
[-   


<a id="org93f588b"></a>

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

\#+begin\_src python 
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

buy = [-sys.maxsize] \* (k+1)
sell = [0] \* (k+1)

for price in prices:
    for i in range(1, k+1):
        buy[i] = max(buy[i], sell[i-1]-price)
        sell[i] = max(sel


<a id="org61b699b"></a>

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

\#+begin\_src python 
  import sys
  class Solution:
      def maxProfit(self, prices):
          dp\_buy = -sys.maxsize
          dp\_sell = 0
          dp\_pre\_0 = 0

for price in prices:
    tmp = dp\_sell
    dp\_sell = max(dp\_sell, dp\_buy + price)
    dp\_buy = max(dp\_buy, dp\_pre\_0 - price)
    dp\_pre\_0 = tmp


<a id="org06a2063"></a>

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

\#+begin\_src python 
  class Solution:
      def maxDepth(self, root):
          return 1 + max(self.maxDepth(root.right), self.maxDepth(


<a id="orgfb8573b"></a>

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

-   


<a id="org43d5a31"></a>

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

    \#+begin\_src python
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
                      return self.isMirrored(left.left, right.right) and \\
                          self.isMirrored(left.right, right.left)
                  else:
                      return False
    \#+end\_sr


<a id="orgb89894b"></a>

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

\#+begin\_src python
  class Solution:
      def rob(self, nums):
          robbed, notRobbed = 0, 0
          for i in nums:
              robbed, notRobbed = notRobbed + i, max(robbed, notRobbed)


<a id="org47da147"></a>

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


### Solution

DP problem.

States: index, dp[index] = longest increasing subsequence at this position

Transition: if nums[j] < nums[i]: dp[i] = max(dp[i], dp[j] + 1) 

Base Case: dp[0] = 1

-   Solution 1: DP with O(n^2)

        class Solution:
            def lengthOfLIS(self, nums):
                dp = [1] * len(nums)
        
                for i in range(1, len(nums)):
                    for j in range(i):
                       if nums[j] < nums[i]:
                           dp[i] = max(dp[i], dp[j] + 1)
        
               return max(dp) if nums else 0

-   Solution 2: DP with binary search for LIS

        class Solution:
            def lengthOfLIS(self, nums):
                if not nums:
                    return 0
                dp = [nums[0]]
                for i in range(1, len(nums)):
                    if nums[i] > dp[-1]:
                        dp.append(nums[i])
                    else:
                        j = self.binarySearch(dp, nums[i])
                        dp[j] = nums[i]
        
                    print(dp)
                return len(dp)
        
            def binarySearch(self, nums, target):
                l = 0
                r = len(nums) - 1
                while l <= r:
                    mid = (l + r) // 2
                    if nums[mid] > target:
                        r = mid - 1
                    elif nums[mid] < target:
                        l = mid + 1
                    else:
                        return mid
        
                return l 
    
    Time: O(nlogn)
    
    Space: O(n)


<a id="org1d673dd"></a>

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


<a id="org8e1d843"></a>

## 152 - Maximum Product Subarray

[leetcode](https://leetcode.com/problems/maximum-product-subarray/)


### Problem

    Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.
    
    Example 1:
    
    Input: [2,3,-2,4]
    Output: 6
    Explanation: [2,3] has the largest product 6.
    Example 2:
    
    Input: [-2,0,-1]
    Output: 0
    Explanation: The result cannot be 2, because [-2,-1] is not a subarray.


### Notes

DP problem:

-   States:
    We have to know two previous states to deduct the current max product:
    
    -   index
    -   max for positive or min for negative
    
    So the DP Table is dp[i(index)][0 or 1(max or min)]

-   Transition:
    -   if nums[i] >= 0:
        dp[i][0] = max(nums[i], dp[i-1][0] \* nums[i])
        dp[i][1] = dp[i-1][1] \* nums[i]
    
    -   if nums[i] < 0:
        
        dp[i][0] = dp[i-1][1] \* nums[i])
        dp[i][1] = min(nums[i], dp[i-1][0] \* nums[i]

-   Base case:
    
    if there is only one element:
    
    dp[0][0] = dp[0][1] = nums[0]


### Solution

-   Solution 1: DP

    Original Version:
    
        class Solution:
            def maxProduct(self, nums):
                if not nums:
                    return 0
        
                dp = [[0] * 2 for i in range(len(nums))]
                res = dp[0][0] = dp[0][1] = nums[0]
        
                for i in range(1, len(nums)):
                    if nums[i] >= 0:
                        dp[i][0] = max(nums[i], dp[i - 1][0] * nums[i])
                        dp[i][1] = dp[i - 1][1] * nums[i]
                    else:
                        dp[i][0] = dp[i - 1][1] * nums[i]
                        dp[i][1] = min(nums[i], nums[i] * dp[i - 1][0])
                    res = max(res, dp[i][0])
                return res
    
    Simplify Version 1:
    
        class Solution:
            def maxProduct(self, nums):
                if not nums:
                    return 0
        
                pos = neg = res = nums[0]
                for i in nums[1:]:
                    if i>=0:
                        pos = max(i, pos*i)
                        neg = neg*i
                    else:
                        tmp = pos # Important: remember the value, because we are gonna alter it.
                        pos = neg*i
                        neg = min(tmp*i, i) # Use the original value
                        # We also can write as this, but we should notice it only works in like python or ruby
                        # pos, neg = neg*i, min(pos*i, i), simplify to version 3
                    res = max(pos, res)
                return res
    
    Simplify Version 2: 
    
        class Solution:
            def maxProduct(self, nums):
                if not nums:
                    return 0
        
                pos = neg = res = nums[0]
                for i in nums[1:]:
                    if i>=0:
                        pos, neg = max(i, pos*i), neg*i
                    else:
                        pos, neg = neg*i, min(i, pos*i)
                    res = max(pos, res)
                return res

-   Solution 2: Prefix sum and Suffix sum

        class Solution:
            def maxProduct(self, nums):
                rnums = nums[::-1]
                for i in range(1, len(nums)):
                    nums[i] *= nums[i-1] or 1
                    rnums[i] *= rnums[i-1] or 1
                return max(nums+rnums)
    
    Time: O(n)
    Space: O(n)


<a id="org8ea3ee2"></a>

## 96 - Unique Binary Search Trees

[leetcode](https://leetcode.com/problems/unique-binary-search-trees/)


### Problem

    Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?
    
    Example:
    
    Input: 3
    Output: 5
    Explanation:
    Given n = 3, there are a total of 5 unique BST's:
    
       1         3     3      2      1
        \       /     /      / \      \
         3     2     1      1   3      2
        /     /       \                 \
       2     1         2                 3


### Notes

-   Solution 1: DP

    In this dp problem, the hard part is to figure out the transition.
    
    -   States: n
    -   Transition:
        
        Some intuition:
        
            assume dp[0] = 1
            dp[1] = dp[0]*dp[0]
            dp[2] = dp[0]*dp[1] + dp[0]*dp[1]
            dp[3] = dp[0]*dp[2] + dp[1]*dp[1] + dp[2]*dp[0]
            dp[4] = dp[0]*dp[3] + dp[1]*dp[2] + dp[2]*dp[1] + dp[3]*dp[0]
            dp[5] = dp[0]*dp[4] + dp[1]*dp[3] + dp[2]*dp[2] + dp[3]*dp[1] + dp[4]*dp[0]
            dp[6] = dp[0]*dp[5] + dp[1]*dp[4] + dp[2]*dp[3] + dp[3]*dp[2] + dp[4]*dp[1] + dp[5]*dp[0]
        
            for i in range(1, n+1):
                for j in range(0, i):
                    dp[i] += dp[j]*dp[i-1-j]
    
    -   Base case:
        dp[0] = 1

-   Solution 2: Catalan Number

    [Catalan Number](https://en.wikipedia.org/wiki/Catalan_number)
    
        Cn = 1/(n+1)(2n n) = (2n)!/(n+1)!n!
        
        The first Catalan numbers for n = 0, 1, 2, 3, ... are
        
        1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, 16796, 58786, 208012, 
        742900, 2674440, 9694845, 35357670, 129644790, 477638700, 1767263190, 
        6564120420, 24466267020, 91482563640, 343059613650, 1289904147324, 4861946401452


### Solution

-   Solution 1: DP

        class Solution:
            def numTrees(self, n):
                if n < 1:
                    return 0
        
                dp = [0] * (n+1)
                dp[0] = 1
        
                for i in range(1, n+1):
                    for j in range(0, i):
                        dp[i] += dp[j]*dp[i-1-j]
        
                return dp[n]

-   Solutiojn 2: Catalan Number

        import math
        class Solution:
            def numTrees(self, n):
                return math.factorial(2*n)/(math.factorial(n)*math.factorial(n+1))


<a id="org08f31e1"></a>

## 221 - Maximal Square

[leetcode](https://leetcode.com/problems/maximal-square/)


### Problem

    Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
    
    Example:
    
    Input: 
    
    1 0 1 0 0
    1 0 1 1 1
    1 1 1 1 1
    1 0 0 1 0
    
    Output: 4


### Notes

DP Problem:

-   States:
    
    -   position -> [i][j]
    -   how many continues 1 in vertical direction -> [i][j][0]
    -   how many continues 1 in horizontal direction -> [i][j][1]
    -   square value(or the length of the square) -> [i][j][2]
    
    dp[i][j][0 or 1 or 2]

-   Transition:
    
        dp[i + 1][j + 1][0] = dp[i][j + 1][0] + 1
        dp[i + 1][j + 1][1] = dp[i + 1][j][1] + 1
        dp[i + 1][j + 1][2] = min(dp[i][j][2]+1, dp[i + 1][j + 1][0], dp[i + 1][j + 1][1])

-   Base Case:
    
    One padding row on vertical and horizontal direction, with value 0


### Solution

-   **Original Version:** 

    class Solution:
        def maximalSquare(self, matrix):
            if not matrix:
                return 0
    
            dp = [[[0] * 3 for j in range(len(matrix[0]) + 1)] for i in range(len(matrix) + 1)]
            res = 0
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if matrix[i][j] == "1":
                        dp[i + 1][j + 1][0] = dp[i][j + 1][0] + 1
                        dp[i + 1][j + 1][1] = dp[i + 1][j][1] + 1
                        dp[i + 1][j + 1][2] = min(dp[i][j][2]+1, dp[i + 1][j + 1][0], dp[i + 1][j + 1][1])
                        res = max(res, dp[i + 1][j + 1][2])
    
            return res*res

Time: O(mn)
Space: O(mn)

-   **Simplified Version 1: optimize the space, 3xn space:** 

    class Solution:
        def maximalSquare(self, matrix):
            if not matrix:
                return 0
    
            dp = [[0] * 3 for j in range(len(matrix[0]) + 1)]
            res = 0
    
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if matrix[i][j] == "1":
                        dp[j+1][0] = dp[j+1][0] + 1
                        dp[j+1][1] = dp[j][1] + 1
                        dp[j+1][2] = min(dp[j+1][2]+1, dp[j+1][0]+1, dp[j][1]+1)
                        res = max(res, dp[j + 1][2])
                    else:
                        dp[j+1][0] = dp[j+1][1] = dp[j+1][2] = 0
    
            return res*res

Space: O(n)

-   **Simplified Version 2: n space:** 

    class Solution:
        def maximalSquare(self, matrix):
            if not matrix:
                return 0
    
            dp = [0 for j in range(len(matrix[0]) + 1)]
            res = 0
            prev = 0 # previous diagnol element
    
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    temp = dp[j+1]
                    if matrix[i][j] == "1":
                        dp[j+1] = min(prev, dp[j+1], dp[j]) + 1
                        res = max(res, dp[j + 1])
                    else:
                        dp[j+1] = 0
    
                    prev = temp
    
            return res*res

-   **Simplified Version 3: in place:** 

    class Solution:
        def maximalSquare(self, matrix):
            if not matrix:
                return 0
            res = 0
            m = len(matrix)
            n = len(matrix[0])
    
            for i in range(m):
                for j in range(n):
                    if matrix[i][j] == "1":
                        if i == 0 or j == 0:
                            matrix[i][j] = 1
                        else:
                            matrix[i][j] = min(matrix[i - 1][j - 1],
                                               matrix[i][j - 1],
                                               matrix[i - 1][j]) + 1
                        res = max(res, matrix[i][j])
                    else:
                        matrix[i][j] = 0
    
            return res * res

Space: O(1)


<a id="orgc00f091"></a>

## 279 - Perfect Squares

[leetcode](https://leetcode.com/problems/perfect-squares/)


### Problem

    Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.
    
    Example 1:
    
    Input: n = 12
    Output: 3 
    Explanation: 12 = 4 + 4 + 4.
    Example 2:
    
    Input: n = 13
    Output: 2
    Explanation: 13 = 4 + 9.


### Notes

DP problem

-   States: n
-   Transition:
-   dp[i] = min([_dp[i-j*j]+1 if i-j*j >= 0 else break for j in range(1, sqrt(i)+1)])

-   Base case:
    -   dp[0] = 0
    -   dp[i] = i


### Solution

    import math
    class Solution:
        dp = [0]
        def numSquares(self, n):
            _dp = self.dp
            if len(_dp) >= n + 1:
                return _dp[n]
            else:
                for i in range(len(_dp), n+1):
                    _dp += [min([_dp[i-j*j]+1 for j in range(1, int(math.sqrt(i))+1) if i-j*j >= 0])] 
            return _dp[n]
    
    print(Solution().numSquares(12))


<a id="org1a92df8"></a>

## 647 - Palindromic Substrings

[leetcode](https://leetcode.com/problems/palindromic-substrings/)


### Problem

    
    Given a string, your task is to count how many palindromic substrings in this string.
    
    The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.
    
    Example 1:
    
    Input: "abc"
    Output: 3
    Explanation: Three palindromic strings: "a", "b", "c".
     
    
    Example 2:
    
    Input: "aaa"
    Output: 6
    Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
    
    Note:
    
    The input string length won't exceed 1000.


### Notes

DP problem

-   States:
    
    left\_index, right\_index, mark if `s[left_index, right_index+1]` is palindromic

-   Transition:
    
        if s[l] == s[r]: # mark it only when both ends are same values
        
        dp[l][r] = 1 if r == l              # if only one element
        dp[l][r] = 1 if r+1 == l            # if only two elements
        dp[l][r] = 1 if dp[l+1][r+1] = 1    # if the string in between is palindromic
        
        results = results + 1

-   Base case:
    
    initialize dp[i][j] = 0


### Solution

    class Solution:
        def countSubstrings(self, s):
            dp = [[0] * len(s) for i in range(len(s))]
            res = 0
            for r in range(len(s)):
                for l in range(r+1):
                    if s[r] == s[l]:
                        if r == l or r+1 == l or dp[l+1][r-1] == 1:
                            dp[l][r] = 1
                            res += 1
            return res
    print(Solution().countSubstrings("aba"))


<a id="org5e53d5f"></a>

## 5 - Longest Palindromic Substring

[leetcode](https://leetcode.com/problems/longest-palindromic-substring/)


### Problem

    Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
    
    Example 1:
    
    Input: "babad"
    Output: "bab"
    Note: "aba" is also a valid answer.
    Example 2:
    
    Input: "cbbd"
    Output: "bb"


### Notes

DP problem

-   States:
    
    left\_index, right\_index, mark if `s[left_index, right_index+1]` is palindromic

-   Transition:
    
        if s[l] == s[r]: # mark it only when both ends are same values
        
        dp[l][r] = 1 if r == l              # if only one element
        dp[l][r] = 1 if r+1 == l            # if only two elements
        dp[l][r] = 1 if dp[l+1][r+1] = 1    # if the string in between is palindromic
        
        results = s[l:r+1] if r-l+1>len(results) # comparing the length, record the maximum

-   Base case:
    
    initialize dp[i][j] = 0


### Solution

-   Solution 1: DP

        class Solution:
            def longestPalindrome(self, s: str) -> str:
                dp = [[0] * len(s) for i in range(len(s))]
                res = ""
                for r in range(len(s)):
                    for l in range(r + 1):
                        if s[l] == s[r]:
                            if l == r or l + 1 == r or dp[l + 1][r - 1] == 1:
                                dp[l][r] = 1
                                if r - l + 1 > len(res):
                                    res = s[l:r + 1]
                return res

-   Solution 2: Central Expansion


<a id="org3b14b89"></a>

## 136 - Single Number

[leetcode](https://leetcode.com/problems/single-number/)


### Problem

    Given a non-empty array of integers, every element appears twice except for one. Find that single one.
    
    Note:
    
    Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
    
    Example 1:
    
    Input: [2,2,1]
    Output: 1
    Example 2:
    
    Input: [4,1,2,1,2]
    Output: 4


### Notes

-   Solution 1: Hash Table

-   Solution 2: Bit manipulation

    Consider XOR all element together. The left number is the single number.


### Solution

-   Solution 1: Hash Table

        class Solution:
            def singleNumber(self, nums):
                table = {}
                for i in nums:
                    table[i] = table.get(i, 0) + 1
                for k in table:
                    if table[k] == 1:
                        return k

-   Solution 2: Bit manipulation for finding the single number

        class Solution:
            def singleNumber(self, nums):
        
                res = 0
        
                for i in nums:
                    res ^= i
        
                return res
        
        print(Solution().singleNumber([2, 2, 5, 1, 8, 1, 9, 8, 9]))

-   Solution 3: Python reduce

        from functools import reduce
        import operator
        nums = [2, 2, 5, 1, 8, 1, 9, 8, 9]
        print(reduce(lambda x, y: x ^ y, nums))
        print(reduce(operator.xor, nums))


<a id="org92fa83a"></a>

## 202 - Happy Number

[leetcode](https://leetcode.com/problems/happy-number/)


### Problem

    Write an algorithm to determine if a number is "happy".
    
    A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.
    
    Example: 
    
    Input: 19
    Output: true
    Explanation: 
    12 + 92 = 82
    82 + 22 = 68
    62 + 82 = 100
    12 + 02 + 02 = 1


### Notes

Hash Table


### Solution

    class Solution:
        def isHappy(self, n):
            table = {}
    
            while n != 1:
                x = n
                n = 0
                while x != 0:
                    n += (x % 10)**2
                    x //= 10
    
                if table.get(n):
                    return False
                else:
                    table[n] = 1
            return True
    
    
    class Solution:
        def isHappy(self, n):
            mem = set()
            while n not in mem:
                mem.add(n)
                n = sum(int(i)**2 for i in str(n))
            return n == 1


<a id="org57e27bb"></a>

## 338 - Counting Bits

[leetcode](https://leetcode.com/problems/counting-bits/)


### Problem

    Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.
    
    Example 1:
    
    Input: 2
    Output: [0,1,1]
    Example 2:
    
    Input: 5
    Output: [0,1,1,2,1,2]


### Notes

DP problem

-   States: index
-   Transition:

    dp[0] = 0
    dp[1] = dp[1-1] + 1 = 1
    dp[2] = dp[2-2] + 1 = 1 
    dp[3] = dp[3-2] + 1 = 2
    dp[4] = dp[4-4] + 1 = 1
    dp[5] = dp[5-4] + 1 = 2
    dp[6] = dp[6-4] + 1 = 2
    dp[7] = dp[7-4] + 1 = 3
    dp[8] = dp[8-8] + 1 = 1
    dp[9] = dp[9-8] + 1 = 2
    dp[i] = dp[i - log_2 (i)] + 1
    
    A trick using bit manipulation:
    
    8 -> 1000
    9 -> 1001
    10 -> 1010
    
    9 & 8 -> 1001 & 1000 -> 1000 dp[8] + 1  = 2
    10 & 9 -> 1010 & 1001 -> 1000 dp[8] + 1 = 2
    11 & 10 -> 1011 & 1010 -> 1010 dp[10] + 1 = 3
    12 & 11 -> 1100 & 1011 -> 1000 dp[8] + 1 = 2
    
    dp[i] = dp[i & (i-1)] + 1


### Solution

-   Solution 1: DP

        class Solution:
            def countBits(self, num):
                offset = 1
                dp = [0] * (num + 1)
                for i in range(1, num + 1):
                    if offset * 2 == i:
                        offset *= 2
                    dp[i] = dp[i - offset] + 1
                return dp

-   Solution 2: Bit manipulation on couting bits

        class Solution:
            def countBits(self, num):
                dp = [0] * (num + 1)
                for i in range(1, num + 1):
                    dp[i] = dp[i & (i - 1)] + 1
                return dp

-   Solution 3:

        class Solution(object):
            def countBits(self, num):
                res=[0]
                while len(res)<=num:
                    res+=[i+1 for i in res]
                return res[:num+1]


<a id="orgd9bf15b"></a>

## 494 - Target Sum

[leetcode](https://leetcode.com/problems/target-sum/)


### Problem

    You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.
    
    Find out how many ways to assign symbols to make sum of integers equal to target S.
    
    Example 1:
    Input: nums is [1, 1, 1, 1, 1], S is 3. 
    Output: 5
    Explanation: 
    
    -1+1+1+1+1 = 3
    +1-1+1+1+1 = 3
    +1+1-1+1+1 = 3
    +1+1+1-1+1 = 3
    +1+1+1+1-1 = 3
    
    There are 5 ways to assign symbols to make the sum of nums be target 3.
    Note:
    The length of the given array is positive and will not exceed 20.
    The sum of elements in the given array will not exceed 1000.
    Your output answer is guaranteed to be fitted in a 32-bit integer.


### Solution

DP problem. The hardest part of this problem is to find the states.

What states do we have to calculate the current result, which is the number of ways of reaching the target.

-   States:
    
    -   index: how many different numbers -> n
    -   sum: how many different possible sums -> [-sum(nums), +sum(nums)]
    
    The tricky part is how you present the range of sum in an array.
    
    You have to add an offest as large as the sum(nums) to shift the range into the positive side.
    
    So it becomes [0, 2sum(nums)]
    
    For example:
    
    [1, 1, 1, 1, 1], you have a range of [-5, 5].
    
    -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5
    
    Add an offset of sum = 5
    
    0,  1,  2,  3,  4, 5, 6, 7, 8, 9, 10  -> 11 numbers
    
    dp should have a length of 2sum(nums) + 1

-   Transition:

We need all the sum values of the previous number to calculate the current one.

    for j in range(2sum+1):
        if dp[i-1][j] > 0: # only check the ones, which have been reached
          if j+nums[i] < 2sum + 1: # sign + to the current number, we transit from j to j+nums[i]
            dp[i][j+nums[i]] += dp[i-1][j]
          if j-nums[i] >= 0: # sign + to the current number, we transit from j to j-nums[i]
            dp[i][j-nums[i]] += dp[i-1][j]

-   Base case:

We start from the offset.

    # the first number with symbols 
    dp[0][offset+nums[0]] +=1
    dp[0][offset-nums[0]] +=1 

**Important**:
You have to use += 1, not only = 1, because the number can be 0.

For exmaple: we take sum = 5
When the first number is 1 (not 0):

    d[0][0+sum + 1] += 1 -> dp[0][6] = 1
    d[0][0+sum - 1] += 1 -> dp[0][4] = 1

It means:

there is one ways to reach 1 (6 - offset)

there is one ways to reach -1 (4 - offset)

When the first number is 0:

    d[0][0+sum + 1] += 1 -> dp[0][5] = 1
    d[0][0+sum - 1] += 1 -> dp[0][5] = 2

It means there are 2 ways to reach 0 (5 - offset)

-   Solution 1: 2D - DP

        class Solution():
            def findTargetSumWays(self, nums, S):
                l = len(nums)
                n = 2 * sum(nums) + 1
                offset = sum(nums)
        
                dp = [[0] * n for i in nums]
        
                if not nums:
                    return 0
        
                # base case
                dp[0][offset - nums[0]] += 1
                dp[0][offset + nums[0]] += 1
        
                for i in range(1, len(nums)):
                    for j in range(n):
                        if dp[i-1][j] > 0:
                            if j + nums[i] < n:
                                dp[i][j + nums[i]] += dp[i-1][j]
                            if j - nums[i] >= 0:
                                dp[i][j - nums[i]] += dp[i-1][j]
        
                return dp[-1][offset + S]
        
        
        print(Solution().findTargetSumWays([1, 1, 1, 1, 1], 3))
    
    Time: O(l\*n)
    Space: O(l\*n)

-   Solution 2: 1D - DP

    We notice that, to calculate the dp array at the current index, we only have to know one previous row.
    
    So we only have to maintain two dp arrays to record previous values and current values respectly.
    
        class Solution:
            def findTargetSumWays(self, nums, S):
                if not nums:
                    return 0
                l = len(nums)
                n = 2 * sum(nums) + 1
                offset = sum(nums)
                dp = [[0] * n for i in nums]
        
                dp[0][offset + nums[0]] += 1
                dp[0][offset - nums[0]] += 1
        
                for i in range(1, l):
                    for j in range(n):
                        if dp[i - 1][j] > 0:
                            if dp[i - 1][j] < n:
                                dp[i][j + nums[i]] += dp[i - 1][j]
                            if dp[i - 1][j] >= 0:
                                dp[i][j - nums[i]] += dp[i - 1][j]
        
                return dp[-1][offset + S]
        
        print(Solution().findTargetSumWays([1, 1, 1, 1, 1], 3))


<a id="org8d901a7"></a>

## 283 - Move Zeros

[leetcode](https://leetcode.com/problems/move-zeroes/)


### Problem

    Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
    
    Example:
    
    Input: [0,1,0,3,12]
    Output: [1,3,12,0,0]
    Note:
    
    You must do this in-place without making a copy of the array.
    Minimize the total number of operations.


### Solution

Two pointers.

One pointer is for the start of 0.

One pointer keeps going forward.

    class Solution:
        def moveZeros(self, nums):
    
            p1, p2 = 0, 0
    
            for p2 < len(nums):
                if nums[p1] != 0:
                    p1 += 1
                elif nums[p2] != 0:
                    nums[p1], nums[p2] = nums[p2], nums[p1]
                    p1 += 1
                p2 += 1
    
            return nums


<a id="org41cd874"></a>

## 416 - Partition Equal Subset Sum

[leetcode](https://leetcode.com/problems/partition-equal-subset-sum/)


### Problem

    Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.
    
    Note:
    
    Each of the array element will not exceed 100.
    The array size will not exceed 200.
     
    
    Example 1:
    
    Input: [1, 5, 11, 5]
    
    Output: true
    
    Explanation: The array can be partitioned as [1, 5, 5] and [11].
     
    
    Example 2:
    
    Input: [1, 2, 3, 5]
    
    Output: false
    
    Explanation: The array cannot be partitioned into equal sum subsets.


### Solution

DP problem, it is similar to problem 494 Target Sum.

Maintain a dp table: dp[i][sum]. Don't forget to the offset. 

Transition:
dp[i][j-nums[i]] += dp[i-1][j]
dp[i][j+nums[i]] += dp[i-1][j]

When the transition is only depend on the last row, usually you always can transform the dp table to 1 dimensional.

-   Solution 1: 1D-DP

        class Solution:
            def canPartition(slef, nums):
                nums_sum = sum(nums)
                if nums_sum % 2 != 0:
                    return False
        
                target = nums_sum//2
                n = target + 1
        
                dp = [False] * n
                dp[0] = True
                for i in range(len(nums)):
                    for j in reversed(range(nums[i], n)):
                        dp[j] = dp[j-nums[i]] or dp[j]
                        if dp[target]:
                            return True
                return dp[target]
    
    Time: O(len(nums)\*sum(nums))
    
    Space: O(len(nums)\*sum(nums))

-   Solution 2: Bit manipulation for maintaning the dp table

        class Solution:
            def canPartition(self, nums):
                s = sum(nums)
                if s%2 != 0:
                    return False
        
                bits = 1
                for i in nums:
                    bits |= bits << i
        
                return (bits >> (s//2)) & 1 == 1
    
    Time: O(n)
    
    Space: O(1) maybe, depends on the sum of the array, the bits can be longer


<a id="orgf324966"></a>

## 698 - Partition to K Equal Sum Subsets

[leetcode](https://leetcode.com/problems/partition-to-k-equal-sum-subsets/)


### Problem

    Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.
    
     
    
    Example 1:
    
    Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
    Output: True
    Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
     
    
    Note:
    
    1 <= k <= len(nums) <= 16.
    0 < nums[i] < 10000.


### Solution


<a id="org65c395e"></a>

## 215 - Kth Largest Element in an Array

[leetcode](https://leetcode.com/problems/kth-largest-element-in-an-array/)


### Problem

    215. Kth Largest Element in an Array
    Medium
    
    3152
    
    222
    
    Add to List
    
    Share
    Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.
    
    Example 1:
    
    Input: [3,2,1,5,6,4] and k = 2
    Output: 5
    Example 2:
    
    Input: [3,2,3,1,2,4,5,5,6] and k = 4
    Output: 4
    Note:
    You may assume k is always valid, 1 ≤ k ≤ array's length.


### Solution

The naive solution would be to maintain an array of length k and update the array 
in each iteration to keep the first kth largest element in the array

-   Solution 1: Array of k

        class Solution:
            def findKthLargest(self, nums, k):
                l = []
        
                for i in nums:
                    if not l:
                        l.append(i)
                    else:
                        len0 = len(l)
                        for j in range(len(l)):
                            if i >= l[j]:
                                l = l[0:j] + [i] + l[j:]
                                break
                        if len0 == len(l) and len0 != k:
                            l.append(i)
                        l = l[0:k]
                return l[-1]
    
    Time: O(nk)
    
    Space: O(k)

-   Solution 2: Partition to find the kth largest

        class Solution:
            def findKthLargest(self, nums, k):
                pos = self.partition(nums, 0, len(nums) - 1)
                if pos + 1 < k:
                    return self.findKthLargest(nums[pos + 1:], k - pos - 1)
                elif pos + 1 > k:
                    return self.findKthLargest(nums[0:pos], k)
                else:
                    return nums[pos]
        
            def partition(self, nums, l, r):
                p = r
        
                while(l < r):
                    while l < r and nums[l] > nums[p]:
                        l += 1
                    while l < r and nums[r] <= nums[p]:
                        r -= 1
                    nums[l], nums[r] = nums[r], nums[l]
                nums[l], nums[p] = nums[p], nums[l]
                return l
    
    Time: O(klogn)
    
    Space: O(1)


<a id="org19f1873"></a>

## 49 - Group Anagrams

[leetcode](https://leetcode.com/problems/group-anagrams/)


### Problem

    Given an array of strings, group anagrams together.
    
    Example:
    
    Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
    Output:
    [
      ["ate","eat","tea"],
      ["nat","tan"],
      ["bat"]
    ]
    Note:
    
    All inputs will be in lowercase.
    The order of your output does not matter.


### Solution

Use the sorted string as key in hash table

    import collections
    class Solution:
        def groupAnagrams(self, strs):
            ans = collections.defaultdict(list)
            for s in strs:
                ans[tuple(sorted(s))].append(s)
            return list(ans.values())

Or use the counter

    import collections
    class Solution:
        def groupAnagrams(self, strs):
            ans = collections.defaultdict(list)
            for s in strs:
                a = [0] * 26
                for c in s:
                    a[ord(c) - ord('a')] += 1
                ans[tuple(a)].append(s)
            return list(ans.values())


<a id="org6c8b5aa"></a>

## 876 - Middle of the Linked List

[leetcode](https://leetcode.com/problems/middle-of-the-linked-list/)


### Problem

    Given a non-empty, singly linked list with head node head, return a middle node of linked list.
    
    If there are two middle nodes, return the second middle node.
    
     
    
    Example 1:
    
    Input: [1,2,3,4,5]
    Output: Node 3 from this list (Serialization: [3,4,5])
    The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
    Note that we returned a ListNode object ans, such that:
    ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.
    Example 2:
    
    Input: [1,2,3,4,5,6]
    Output: Node 4 from this list (Serialization: [4,5,6])
    Since the list has two middle nodes with values 3 and 4, we return the second one.


### Solution

-   Solution 1: two-pointer

        class Solution:
            def middleNode(self, head: ListNode) -> ListNode:
                p1 = p2 = head
                while p2 and p2.next:
                    p2 = p2.next.next
                    p1 = p1.next
        
                return p1

-   Solution 2: counter

        class Solution:
            def middleNode(self, head):
                mid = head
                count = 0
                while head:
                    count += 1
                    if count % 2 == 0:
                        mid = mid.next
                    head = head.next
                return mid

