class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words: 
            return []
        length = len(words[0])
        total_words = len(words)
        words = Counter(words)
        ans = []
        def dfs(start, i, path):
            if len(path) == total_words:
                ans.append(start)
                return
            if i >= len(s):
                return 
            w = s[i:i+length]    
            if words[w]:
                words[w] -= 1
                dfs(start, i+length, path+[w])
                words[w] += 1 
                
        for i in range(len(s)-length*total_words+1):
            dfs(i, i, [])
            
        return ans
