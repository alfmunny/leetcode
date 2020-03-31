
# 5 - Longest Palindromic Substring

[leetcode](https://leetcode.com/problems/longest-palindromic-substring/)


## Problem

    Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
    
    Example 1:
    
    Input: "babad"
    Output: "bab"
    Note: "aba" is also a valid answer.
    Example 2:
    
    Input: "cbbd"
    Output: "bb"


## Notes

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


## Solution


### Solution 1: DP

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


### TODO Solution 2: Central Expansion

