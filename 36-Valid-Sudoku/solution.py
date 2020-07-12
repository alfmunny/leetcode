class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            nums = [x for x in row if x != '.' ]
            if self.notValid(nums):
                return False
            
        for i in range(len(board[0])):
            col = [row[i] for row in board]
            nums = [x for x in col if x != '.' ]
            if self.notValid(nums):
                return False
            
        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                nums = [x for row in board[i:i+3] for x in row[j:j+3] if x != '.']
                if self.notValid(nums):
                    return False
        return True
    
    def notValid(self, nums):
        return len(set(nums)) != len(nums)
