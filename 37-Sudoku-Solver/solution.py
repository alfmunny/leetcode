class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.finish = False
        self.solve(board, 0, 0)

    def solve(self, board, i, j):
        if i >= len(board):
            self.finish = True
            return
        next_i, next_j = i + (j + 1) // 9, (j + 1) % 9
        if board[i][j] == '.':
            for n in range(1, 10):
                if self.is_safe(board, i, j, str(n)):
                    board[i][j] = str(n)
                    self.solve(board, next_i, next_j)
                    if self.finish:
                        return
                    board[i][j] = '.'
        else:
            self.solve(board, next_i, next_j)

    def is_safe(self, board, i, j, n):
        return self.is_safe_vertical(
            board, i, j, n) and self.is_safe_horizontal(
                board, i, j, n) and self.is_safe_sub(board, i, j, n)

    def is_safe_vertical(self, board, i, j, n):
        return n not in [a[j] for a in board]

    def is_safe_horizontal(self, board, i, j, n):
        return n not in board[i]

    def is_safe_sub(self, board, i, j, n):
        p1 = i // 3 * 3
        p2 = j // 3 * 3
        for x in range(p1, p1 + 3):
            for y in range(p2, p2 + 3):
                if board[x][y] == n:
                    return False
        return True
