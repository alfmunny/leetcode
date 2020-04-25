# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:
class Solution:
    def leftMostColumnWithOne(self, binaryMatrix):
        n, m = binaryMatrix.dimensions()
        ans = m
        for i in range(n):
            x = self.findOne(binaryMatrix, i, 0, m - 1)
            if x != -1:
                ans = min(ans, x)
        return ans if ans != m else -1
                
    def findOne(self, m, r, i, j):
        if i == j:
            return i if m.get(r, i) == 1 else -1
        
        mid = (i + j) // 2
        if m.get(r, mid) == 1:
            if mid == 0 or m.get(r, mid - 1) == 0:
                return mid
            else:
                return self.findOne(m, r, i, mid - 1)
        else:
            return self.findOne(m, r, mid+1, j)
