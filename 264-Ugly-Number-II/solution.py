class Solution:
    ugly = sorted(2**a * 3**b * 5**c for a in range(32) for b in range(32) for c in range(32))
    def nthUglyNumber(self, n: int) -> int:
        return self.ugly[n-1]
