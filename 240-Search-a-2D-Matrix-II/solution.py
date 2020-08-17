class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        
        j = 0
    
        for row in matrix:
            if row[j] > target:
                while row[j] > target:
                    j -= 1
                    if j < 0:
                        return False

                
            elif row[j] < target:
                while row[j] < target:
                    j += 1
                    if j == len(matrix[0]):
                        j = 0
                        break
            
            
            if row[j] == target:
                return True
            
        return False
