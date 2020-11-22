class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ret = []
        self.dfs(graph, 0, [0], ret)
        return ret
    
    def dfs(self, graph, source, path, ret):
        
        if source == len(graph) - 1:
            ret.append(list(path))
            
        for w in graph[source]:
            self.dfs(graph, w, path+[w], ret)
