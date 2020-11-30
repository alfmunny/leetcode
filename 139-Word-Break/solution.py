class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        
        def dfs(index):
            if index in memo: return memo[index]
            if index >= len(s): return True
            
            ret = False
            for i in range(index+1, len(s)+1):
                if s[index:i] in wordDict:
                    if dfs(i):
                        ret = True
                        break
                        
            memo[index] = ret
            return ret
        
        return dfs(0)
