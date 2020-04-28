class Solution:
    def majorityElement(self, nums):
        counter = 1
        ans = nums[0]

        for n in nums[1:]:
            if n == ans:
                counter += 1
            else:
                counter -= 1
                if counter < 0:
                    counter = 1
                    ans = n
        return ans
print(Solution().majorityElement([1, 1, 2, 2, 2, 2, 4]))
