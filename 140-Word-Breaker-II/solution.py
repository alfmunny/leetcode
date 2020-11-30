class Solution(object):
    def wordBreak(self, s, wordDict):
        return self.dfs(s, set(wordDict), 0, {})
        
    def dfs(self, s, wordDict, start, memo):
        
        if start >= len(s): return [""]
        if start in memo: return memo[start]
                
        ans = []
        for i in range(start+1, len(s)+1):
            w = s[start:i]
            if w in wordDict:
                ans += [" ".join([w, x]) if x else w for x in self.dfs(s, wordDict, i, memo)]
                
        memo[start] = ans
        return ans
