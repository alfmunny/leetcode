class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        self.dfs(s, 0, ans, [])
        return ans
    
    def dfs(self, s, index, ans, path):
        
        if index == len(s):
            ans.append(list(path))
            return
        
        for i in range(index, len(s)):
            w = s[index:i+1]
            if self.palindrome(w):
                path.append(w)
                self.dfs(s, i+1, ans, path)
                path.pop()
            
                
    def palindrome(self, w):
        for i in range(0, len(w)//2):
            if w[i] != w[len(w) - 1 -i]:
                return False
            
        return True
