class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        ans = [0] * n
        ans[0] = 1

        for i in range(1, n):
            ans[i] = ans[i-1] * nums[i-1]

        R = 1
        for i in reversed(range(n)):
            ans[i] = ans[i] * R
            R *= nums[i]
            
        return ans

print(Solution().productExceptSelf([1, 2, 3, 4]))
