class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"
        
        for i in range(n-1):
            say = s[0]
            count = 0
            tmp = ""
            for c in s:
                if c == say:
                    count += 1
                else:
                    tmp = tmp + str(count) + say
                    say = c
                    count = 1
            s = tmp + str(count) + say
        return s
