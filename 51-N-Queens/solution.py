class Solution:
    def solveNQueens(self, n):
        ans = []
        
        self.dfs(0, n, [], ans)
        return ans
    
    def dfs(self, row, n, path, ans):
        if row == n and len(path) == n:
            ans.append(self.draw(path, n))        
        for i in range(n):
            if self.attack(path, row, i):
                continue    
            path.append([row, i])
            self.dfs(row+1, n, path, ans)
            path.pop()
            
    def attack(self, path, row, i):
        for pair in path:
            if pair[1] == i:
                return True
            elif abs(row - pair[0]) == abs(i - pair[1]):
                return True
        return False
    
    def draw(self, path, n):
        ans = []
        for pair in path:
            ans.append("." * pair[1] + "Q" + "." * (n-1-pair[1]))
            
        return ans
