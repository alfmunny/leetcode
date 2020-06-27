class Solution:
    def isUgly(self, num: int) -> bool:
        if num <= 0:
            return False
        
        while num != 1:
            tmp = num
            for n in [2, 3, 5]:
                if num % n == 0:
                    num //= n
            if tmp == num:
                return False
        return True
