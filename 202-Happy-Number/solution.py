class Solution:
    def isHappy(self, n):
        table = {}

        while n != 1:
            x = n
            n = 0
            while x != 0:
                n += (x % 10)**2
                x //= 10

            if table.get(n):
                return False
            else:
                table[n] = 1
        return True


class Solution:
    def isHappy(self, n):
        mem = set()
        while n not in mem:
            mem.add(n)
            n = sum(int(i)**2 for i in str(n))
        return n == 1
