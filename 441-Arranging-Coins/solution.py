class Solution:
    def arrangeCoins(self, n: int) -> int:
        k = 0
        while n > 0:
            k += 1
            n -= k
            
        return k if not n else k - 1
