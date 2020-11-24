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
