class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        count = sum([ (-1+2*x)*y for x, y in shift ]) % len(s)
        ds = s + s
        return ds[len(s)-count: 2*len(s) - count]
