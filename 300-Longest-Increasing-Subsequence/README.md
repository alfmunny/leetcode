
# 300 - Longest Increasing Subsequence

[leetcode](https://leetcode.com/problems/longest-increasing-subsequence/)


## Problem

    Given an unsorted array of integers, find the length of longest increasing subsequence.
    
    Example:
    
    Input: [10,9,2,5,3,7,101,18]
    Output: 4 
    Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
    Note:
    
    There may be more than one LIS combination, it is only necessary for you to return the length.
    Your algorithm should run in O(n2) complexity.
    Follow up: Could you improve it to O(n log n) time complexity?


## Notes


### Solution 1: DP with O(n^2)

DP problem

States: index, dp[index] = longest increasing subsequence at this position

Transition: if nums[j] < nums[i]: dp[i] = max(dp[i], dp[j] + 1) 

Base Case: dp[0] = 1


### Solution 2: DP with binary search


## Solution


### Solution 1: DP with O(n^2)

    class Solution:
        def lengthOfLIS(self, nums):
            dp = [1] * len(nums)
    
            for i in range(1, len(nums)):
                for j in range(i):
                    if nums[j] < nums[i]:
                        dp[i] = max(dp[i], dp[j] + 1)
    
            return max(dp) if nums else 0


### TODO Solution 2: DP with binary search


# 322 - Coin Change

[leetcode](https://leetcode.com/problems/coin-change/)


## Problem

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


## Notes

DP problem

States: amount

Transition: dp[i] = min(dp[i], dp[i-coins[j]]+1)


## Solution

    class Solution:
        def coinChange(self, coins, amount):
            dp = [float('inf')] * (amount + 1)
    
            dp[0] = 0
    
            for i in range(1, amount + 1):
                for j in range(len(coins)):
                    if i - coins[j] >= 0:
                        dp[i] = min(dp[i], dp[i - coins[j]] + 1)
    
            return dp[-1] if dp[-1] != float('inf') else -1

