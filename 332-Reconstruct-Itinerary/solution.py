class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        edges = defaultdict(list)
        
        for v, w in sorted(tickets)[::-1]:
            edges[v] += [w]
        path = []    
        self.dfs("JFK", edges, path)
        return path[::-1]
    
    def dfs(self, vertice, edges, path):
        while(edges[vertice]):
            self.dfs(edges[vertice].pop(), edges, path)
        path.append(vertice)
