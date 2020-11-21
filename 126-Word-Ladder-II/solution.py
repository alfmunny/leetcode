class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]):
        if endWord not in wordList:
            return []
        
        h = Counter(set(wordList))
        paths = defaultdict(set)
        queue = [beginWord]
        h[beginWord] = 0
        levels = []
        seen = False
        while queue and not seen:
            tmp = []
            while queue:
                w = queue.pop()
                if w == endWord:
                    seen = True
                for i in range(len(w)):
                    for j in range(26):
                        to = w[:i] + chr(ord('a') + j) + w[i+1:]
                        if to != w and h[to]:
                            tmp.append(to)
                            paths[w].add(to)
            for t in tmp:
                h[t] = 0
            
            levels.append(list(tmp))
            queue = tmp
                
        ret = []
        self.dfs(beginWord, endWord, paths, [], ret)
        return ret

    def dfs(self, beginWord, endWord, paths, path, ret):
        if beginWord == endWord:
            ret.append(path+[beginWord])
            return
        
        for x in paths[beginWord]:
            self.dfs(x, endWord, paths, path+[beginWord], ret)
