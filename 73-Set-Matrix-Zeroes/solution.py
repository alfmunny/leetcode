class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        col_zero = False
        
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                col_zero = True
            for j in range(1, len(matrix[0])):  
                if matrix[i][j] == 0:
                    matrix[0][j] = matrix[i][0] = 0
                    
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if not matrix[0][j] or not matrix[i][0]:
                    matrix[i][j] = 0
                
        if matrix[0][0] == 0:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0
                
        if col_zero:
            for i in range(len(matrix)):
                matrix[i][0] = 0
