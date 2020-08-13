class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False
        
        left = 0
        right = len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return True

            while left < mid and nums[left] == nums[mid]:
                left += 1
                
            if nums[mid] >= nums[left]:
                if nums[mid] > target >= nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            print(left, right)
                    
        return target == nums[left]
