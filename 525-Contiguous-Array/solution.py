class Solution:
    def findMaxLength(self, nums):
        h = {0: -1}

        count = ans = 0
        for i in range(len(nums)):
            count += 1 if nums[0] else -1
            ans = max(ans, h.setdefault(count, i))

        return ans
