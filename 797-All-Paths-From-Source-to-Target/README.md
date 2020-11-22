# 797 - All Paths From Source to Target

[leetcode](https://leetcode.com/problems/all-paths-from-source-to-target/)

## Problem

    Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1, and return them in any order.
    
    The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).

## Solution

```python
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
```
