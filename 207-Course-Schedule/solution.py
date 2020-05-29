class Solution:
    def canFinish(self, numCourses, prerequisites):
        self.hasCycle = False
        self.adj = [[] for _ in range(numCourses)]
        self.marked = [0] * numCourses
        self.stack = [0] * numCourses

        for pre in prerequisite:
            v, w = pre
            adj[v].append(w)

        for v in range(numCourses):
            if not self.marked[v]:
                self.dfs(v)

        return not self.hasCycle

    def dfs(self, v):
        self.marked[v] = 1
        self.stack[v] = 1

        for w in self.adj[v]:
            if self.hasCycle:
                return
            elif not self.marked[w]:
                self.dfs(w)
            elif self.stack[w]:
                self.hasCycle = True
