class Solution:
    def bitwiseComplement(self, num):
        x = 1
        while x < num: x = 2 * x + 1
        return x - num
