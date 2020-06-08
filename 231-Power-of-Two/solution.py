class Solution:
    def powerOfTwo(self, n):
        return n and not (n & n-1)
