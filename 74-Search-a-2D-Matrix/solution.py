class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        rl, rr = 0, len(matrix) - 1
        cl, cr = 0, len(matrix[0]) - 1
        
        while rl <= rr:
            mid = (rl + rr) // 2
            if target < matrix[mid][0]:
                rr = mid - 1
            elif target > matrix[mid][-1]:
                rl = mid + 1
            else:
                rl = mid
                break
                
        if rl > rr:
            return False
        
        while cl <= cr:
            mid = (cl + cr) // 2
            
            if target < matrix[rl][mid]:
                cr = mid - 1
            elif target > matrix[rl][mid]:
                cl = mid + 1
            else:
                return True
            
        return False
