class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        marked = [[False] * len(board[0]) for _ in board]

        for i in range(len(board)):
            for j in range(len(board[0])):
                self.flag = False
                if board[i][j] == 'O' and not marked[i][j]:
                    self.dfs(i, j, board, marked)

                    if not self.flag:
                        self.color(i, j, board)

    def dfs(self, i, j, board, marked):
        marked[i][j] = True

        for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
                self.flag = True
                continue

            if marked[x][y]:
                continue

            if board[x][y] == 'O':
                self.dfs(x, y, board, marked)

    def color(self, i, j, board):
        board[i][j] = 'X'
        for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            if board[x][y] == 'O':
                self.color(x, y, board)
