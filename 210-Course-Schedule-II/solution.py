class Solution:
    def canFinish(self, numCourses, prerequisites):
        adj = [[] for _ in range(numCourses)]
        degree = [0] * numCourses

        for pre in prerequisites:
            v, w = pre
            adj[w].append(v)
            degree[v] += 1

        q = [v for v in range(numCourses) if not degree[v]]
        order = []

        while q:
            v = q.pop(0)
            order.append(v)
            for w in adj[v]:
                degree[w] -= 1
                if not degree[w]:
                    q.append(w)

        return len(order) == numCourses
