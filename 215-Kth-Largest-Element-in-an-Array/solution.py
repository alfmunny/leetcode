class Solution:
    def findKthLargest(self, nums, k):
        pos = self.partition(nums, 0, len(nums) - 1)
        if pos + 1 < k:
            return self.findKthLargest(nums[pos + 1:], k - pos - 1)
        elif pos + 1 > k:
            return self.findKthLargest(nums[0:pos], k)
        else:
            return nums[pos]

    def partition(self, nums, l, r):
        # 1, 5 ,9, 2, 4, 6, 8, 5
        p = r

        while(l < r):
            while l < r and nums[l] > nums[p]:
                l += 1
            while l < r and nums[r] <= nums[p]:
                r -= 1
                
            nums[l], nums[r] = nums[r], nums[l]

        nums[l], nums[p] = nums[p], nums[l]
        print(nums)

        return l
