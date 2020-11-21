class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        h = Counter(set(wordList))
        
        queue = [beginWord]
        ret = 1
        
        while queue:
            tmp = []
            while queue:
                w = queue.pop()
                if w == endWord:
                    return ret
                
                for i in range(len(w)):
                    for j in range(26):
                        to = w[:i] + chr(ord('a') + j) + w[i+1:]
                        if to != w and h[to]:
                            tmp.append(to)
                            h[to] = 0
            ret += 1
            queue = tmp
        return 0
