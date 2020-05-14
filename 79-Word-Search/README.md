# 79 - Word Search

[leetcode](https://leetcode.com/problems/word-search/)

## Problem

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

## Notes

Backtrack problem.

1.  when found, mark the point to one.
2.  Use dfs to go down from this point.
3.  Can't go down anymore, mark the point back to zero (backtrack step).

## Solution

### Solution 1: Backtrack, dfs

```python
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
```
