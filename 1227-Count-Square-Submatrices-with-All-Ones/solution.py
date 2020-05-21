class Solution:
    def countSquares(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    if i and j:
                        matrix[i][j] = min(matrix[i-1][j-1], matrix[i][j-1], matrix[i-1][j]) + 1
                    ans += matrix[i][j]
        return ans
