class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        ans = [i for i in range(1, 10)]

        if N == 1:
            return [0] + ans

        digits = 10 ** (N-1)

        while ans[0] / digits < 1:
            cur = ans.pop(0)
            last_digit = cur % 10
            if K == 0:
                ans.append(cur * 10 + last_digit)
            else:
                if last_digit + K < 10:
                    ans.append(cur * 10 + last_digit + K)
                if last_digit - K >= 0:
                    ans.append(cur * 10 + last_digit - K)
        return ans
