# 130 - Surrounded Regions

[leetcode](https://leetcode.com/explore/featured/card/june-leetcoding-challenge/541/week-3-june-15th-june-21st/3363/)

## Problem

    Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.
    
    A region is captured by flipping all 'O's into 'X's in that surrounded region.
    
    Example:
    
    X X X X
    X O O X
    X X O X
    X O X X
    After running your function, the board should be:
    
    X X X X
    X X X X
    X X X X
    X O X X
    Explanation:
    
    Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'.
    Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'.
    Two cells are connected if they are adjacent cells connected horizontally or vertically.

## Solution

```python
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        marked = [[False] * len(board[0]) for _ in board]

        for i in [0, len(board)-1]:
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    self.color(board, i, j, 'O', 'S')

        for i in range(1, len(board)-1):
            for j in [0, len(board[0])-1]:
                if board[i][j] == 'O':
                    self.color(board, i, j, 'O', 'S')

        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = 'OX'[board[i][j] !='S']


    def color(self, board, i, j, target, symbol):
        if i >= len(board) or j >= len(board[0]) or i < 0 or j < 0:
            return

        if board[i][j] == target:
            board[i][j] = symbol
            for v, w in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                self.color(board, i+v, j+w, target, symbol)
```
