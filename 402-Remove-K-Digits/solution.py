class Solution:
    def removeKdigits(self, num, k):
        stack = []
        for c in num:
            while k and stack and stack[-1] > c:
                stack.pop()
                k -= 1
            stack.append(c)

        return ''.join(stack[:-k or None]).lstrip('0') or '0'
