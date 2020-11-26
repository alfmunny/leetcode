class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        self.upper_bound = 2**31-1
        self.ret = []
        
        self.dfs(S, 0, [], [])
        
        return self.ret
    
    def dfs(self, S, index, ret, path):
        if self.ret:
            return
        
        if index == len(S) and "".join(map(str, ret)) == S and len(ret) >= 3:
            self.ret = list(ret)
            return
        elif index == len(S):
            return
        
        path.append(S[index])

        n = int("".join(path))
        if self.isFibonacci(ret, n):
            self.dfs(S, index+1, ret+[n], [])
            
        self.dfs(S, index+1, ret, path)
        path.pop()
        
    def isFibonacci(self, sequence, number):
        if number < 0 or number > self.upper_bound:
            return False
        
        if len(sequence) < 2:
            return True
        
        return True if number == sequence[-1] + sequence[-2] else False
