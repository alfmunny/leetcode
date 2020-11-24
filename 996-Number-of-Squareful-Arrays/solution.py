class Solution:
    def numSquarefulPerms(self, A: List[int]) -> int:
        self.h = defaultdict(bool)
        
        mark = [False] * len(A)
        self.ret = 0
        self.dfs(sorted(A), [], mark)
        return self.ret 
        
    def dfs(self, A, path, mark):
        
        if len(path) == len(A):
            self.ret += 1
        
        for i, v in enumerate(A):
            if (i > 0 and A[i] == A[i-1] and not mark[i-1]) or mark[i]:
                continue
            if not path or self.isSquare(path[-1]+v):
                mark[i] = True
                self.dfs(A, path+[v], mark)
                mark[i] = False
        
    def isSquare(self, num):
        return True if int((num**0.5))**2 == num else False
