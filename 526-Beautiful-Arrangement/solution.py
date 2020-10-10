class Solution:
    def countArrangement(self, N: int) -> int:
        self.ans = 0
        self.mark = [False for i in range(N+1)]
        self.dfs(N, self.mark, [])
        return self.ans
    
    def dfs(self, N, mark, path):
        if len(path) == N:
            self.ans += 1
        
        for n in range(1, N+1):
            index = len(path) + 1
            if mark[n] or (n % index != 0 and index % n != 0):
                continue    
            mark[n] = True
            self.dfs(N, self.mark, path + [n])
            mark[n] = False
