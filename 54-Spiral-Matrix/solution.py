class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        i = j = 0
        m = len(matrix)
        n = len(matrix[0])
        marked = [[False] * n for _ in matrix]
        step = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        i = j = di = 0
        ans = []
        for _ in range(m*n):
            ans.append(matrix[i][j])
            marked[i][j] = True
            ni, nj = i + step[di][0], j + step[di][1]
            
            if 0 <= ni < m and 0 <= nj < n and not marked[ni][nj]:
                i, j = ni, nj
            else:
                di = (di + 1) % 4
                i, j = i+step[di][0], j + step[di][1]                                                       
                                                                  
        return ans
