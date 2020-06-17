class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        
        for i in range(1, numRows+1):
            level = [1] * i
            
            if ans:
                for j in range(1, i-1):
                    level[j] = ans[-1][j-1] + ans[-1][j]
                    
            ans.append(level)
            
        return ans
