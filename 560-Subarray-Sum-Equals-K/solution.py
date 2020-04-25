class Solution:
    def subArraySum(self, nums, k):
        h = {0: 1}
        s = 0
        ans = 0
        for i in nums:
            s += i
            ans += h.get(s-k, 0)
            h[s] = h.get(s, 0) + 1

        return ans
