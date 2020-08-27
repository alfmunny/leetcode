class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]: 
        if len(s) > 12:
            return []
        
        ans = []
        self.dfs(s, 0, ans, [])
        return ans
    
    def dfs(self, s, start, ans, path):
        if start >= len(s):
            if len(path) == 4:
                ans.append(".".join(path))
            return

        for i in range(start, min(len(s), start+3)):
            number = s[start:i+1]
            if len(number) > 1 and number[0] == "0":
                continue
                
            if int(number) <= 255:
                path.append(number)
                self.dfs(s, i+1, ans, path)
                path.pop()
