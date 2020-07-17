class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        z = x ^ y
        s = 0
        while z:

            s += 1
            z = z & (z - 1)

        return s
