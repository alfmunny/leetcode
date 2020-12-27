class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        
        graph = defaultdict(list)
        
        self.connect(graph, root, root.left)
        self.connect(graph, root, root.right)
        level = [target.val]
        marked = set(level)
        for i in range(K):
            new_level = []
            for x in level:
                for w in graph[x]:
                    if w not in marked:
                        new_level.append(w)
            level = new_level
            marked |= set(new_level)
            
        return level
        
    def connect(self, graph, parent, child):
        if parent and child:
            graph[parent.val].append(child.val)
            graph[child.val].append(parent.val)
        
            self.connect(graph, child, child.left)
            self.connect(graph, child, child.right)
