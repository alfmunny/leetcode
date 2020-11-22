class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        h = {}
        def canIWinRec(numbers, desiredTotal):
            if numbers[-1] >= desiredTotal:
                return True

            k = tuple(numbers)
            if k in h:
                return h[k]

            for i in range(len(numbers)):
                if not canIWinRec(numbers[:i] + numbers[i+1:], desiredTotal - numbers[i]):
                    h[k] = True
                    return True

            h[k] = False
            return False
        
        summed = (maxChoosableInteger + 1) * maxChoosableInteger / 2

        if summed < desiredTotal:
            return False
        
        if summed == desiredTotal:
            return maxChoosableInteger % 2    
        
        numbers = list(range(1, maxChoosableInteger+1))
        return canIWinRec(numbers, desiredTotal)
