class Solution:
    def singleNonDuplicate(self, nums):
        lo = 0
        hi = len(nums) - 1

        while lo < hi:
            mid = (lo + hi) // 2
            if mid == 0:
                return mid

            if (mid - lo + 1) % 2 == 0:
                if nums[mid] == nums[mid - 1]:
                    lo = mid + 1
                else:
                    hi = mid - 1
            else:
                if nums[mid] == nums[mid - 1]:
                    hi = mid - 2
                else:
                    lo = mid
        return nums[lo]
    
print(Solution().singleNonDuplicate([1,1,2,3,3,5,5,10,10]))
