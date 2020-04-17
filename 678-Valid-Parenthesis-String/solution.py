class Solution:
    def checkValidString(self, s: str) -> bool:
        counter_max = 0
        counter_min = 0
        
        for c in s:
            if c == "(":
                counter_max += 1
                counter_min += 1
            elif c == ")":
                counter_max -= 1
                counter_min = max(counter_min-1, 0)
            else:
                counter_max += 1
                counter_min = max(counter_min-1, 0)
                
            if counter_max < 0:
                return False
            
        return counter_min == 0
