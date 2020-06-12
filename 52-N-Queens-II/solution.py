class Solution:
    def totalNQueens(self, n):
        self.ans = 0
        self.dfs(0, n, [])
        return self.ans
    
    def dfs(self, row, n, path):
        if row == n and len(path) == n:
            self.ans += 1        
        for i in range(n):
            if self.attack(path, row, i):
                continue    
            path.append([row, i])
            self.dfs(row+1, n, path)
            path.pop()
            
    def attack(self, path, row, i):
        for pair in path:
            if pair[1] == i:
                return True
            elif abs(row - pair[0]) == abs(i - pair[1]):
                return True
        return False
