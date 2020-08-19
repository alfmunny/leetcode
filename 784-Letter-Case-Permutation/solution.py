class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        ans = []
        self.dfs(S, 0, ans, [])
        return ans
        
    def dfs(self, S, i, ans, path):
        if i == len(S):
            ans.append(''.join(path))
            return
        
        self.dfs(S, i+1, ans, path + [S[i]])
        
        if S[i].isalpha():
            self.dfs(S, i+1, ans, path + [S[i].swapcase()])
