
# LeetCode


# Table of Contents

-   [LeetCode](#org8b89394)
    -   [41. First Missing Positive](#org7a03aec)
    -   [48. Rotate Image](#org4a8614f)
    -   [53. Maximum Subarray](#orgc8179d6)
    -   [55. Jump Game](#org5b8fbf2)
    -   [62. Unique Paths](#org1c34e28)
    -   [91. Decode Ways](#orgbe9a3df)
    -   [70. Climbing Stairs](#org9732d35)
    -   [509. Fibonacci Number](#orgd14b2a5)


<a id="org7a03aec"></a>

## [41. First Missing Positive](https://leetcode.com/problems/first-missing-positive/)


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


### Notes:

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


### Solution:

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
    
    print(Solution().firstMissingPositive([1, -1, 3, 4]))


<a id="org4a8614f"></a>

## [48. Rotate Image](https://leetcode.com/problems/rotate-image/)


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


<a id="orgc8179d6"></a>

## [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)


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


<a id="org5b8fbf2"></a>

## [55. Jump Game](https://leetcode.com/problems/jump-game/)


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


<a id="org1c34e28"></a>

## [62. Unique Paths](https://leetcode.com/problems/unique-paths/)


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


<a id="orgbe9a3df"></a>

## [91. Decode Ways](https://leetcode.com/problems/decode-ways)


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


<a id="org9732d35"></a>

## [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)


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


<a id="orgd14b2a5"></a>

## 509. Fibonacci Number

