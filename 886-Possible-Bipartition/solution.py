class Solution:
    def possibleBipartition(self, N: int, dislikes):
        self.graph = [[] for _ in range(N+1)]
        self.marked = [0] * (N+1)
        
        for pair in dislikes:
            v, w = pair
            self.graph[v].append(w)
            self.graph[w].append(v)
        
        for v in range(1, N+1):
            if not self.marked[v] and not self.dfs(v, 1):
                return False
        return True    
                
    def dfs(self, v, color):
        self.marked[v] = color
        for w in self.graph[v]:
            if not self.marked[w] and not self.dfs(w, -color):
                return False
            elif self.marked[w] == color:
                return False
            
        return True
