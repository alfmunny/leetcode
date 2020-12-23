from collections import defaultdict

class Solution():
    def ConnectedComponents(self, edges):
      graph = defaultdict(list)
      marked = {}
      for edge in edges:
          graph[edge[0]].append(edge[1])
          graph[edge[1]].append(edge[0])
          marked[edge[0]] = False
          marked[edge[1]] = False
          
      ans = 0
      for v in graph.keys():
          if not marked[v]:
              self.dfs(graph, v, marked)
              ans += 1
      return ans
  
    def dfs(self, graph, v, marked):
        marked[v] = True
        for w in graph[v]:
            if not marked[w]:
                self.dfs(graph, w, marked)

print(Solution().ConnectedComponents([[0, 1], [1, 2], [3, 4]]))
