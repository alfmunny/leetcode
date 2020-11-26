class Solution:
    def nextGreaterElement(self, n: int) -> int:
        s = list(str(n))
        
        first = len(s) - 1
        for i in range(len(s)-2, -1, -1):
            if s[i] < s[i+1]:
                first = i
                break
                
        if first == len(s) - 1:
            return -1

        second = first+1
        minimum = s[second]
        
        for i in range(first+1, len(s)):
            if s[i] < minimum and s[i] > s[first]:
                minumum = s[i]
                second = i
        
        s[first], s[second] = s[second], s[first]
        
        ret = int("".join(s[:first+1] + sorted(s[first+1:])))
        return ret if ret <= (1<<31-1) else -1
