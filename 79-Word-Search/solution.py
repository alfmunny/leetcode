class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, word, 0, i, j):
                    return True
        return False

    def dfs(self, board, word, w, i, j):
        if w == len(word):
            return True

        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
            return False

        if board[i][j] == word[w]:
            board[i][j] = '-'

            for next_i, next_j in [[i + 1, j], [i - 1, j], [i, j - 1],
                                   [i, j + 1]]:
                if self.dfs(board, word, w + 1, next_i, next_j):
                    return True

            board[i][j] = word[w]

        return False
