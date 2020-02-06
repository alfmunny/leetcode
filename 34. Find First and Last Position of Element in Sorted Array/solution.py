class Solution(object):
  def searchRange(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    l, r = 0, len(nums) - 1
    res = [-1, -1]

    if len(nums) == 0:
      return res

    # find the leftmost one
    while (l < r):
      mid = (l + r) // 2

      # always move left pointer if target is not found
      if nums[mid] < target:
        l = mid + 1
      else: # always move the right pointer if the target is found or in the right part
        r = mid

    # No target found
    if nums[l] != target:
      return res

    res[0] = l


    # find the rightmost one
    # l is already the leftmost one,
    # we only have to reset the right pointer
    r = len(nums) - 1

    while l < r:
      # biased on the right
      mid = (l + r) // 2 + 1

      if nums[mid] > target:
        r = mid - 1
      else:
        l = mid


    res[1] = l
    return res


  def findLeftmost(self, nums, target):
    if len(nums) == 0:
      return -1

    l, r = 0, len(nums) - 1
    while l < r:
      mid = (l + r) // 2

      if target > nums[mid]:
        l = mid + 1
      else:
        r = mid

    return l if nums[l] == target else -1

  def findRightmost(self, nums, target):

    if len(nums) == 0:
      return -1

    l, r = 0, len(nums) - 1

    while l < r:
      mid = (l + r) // 2 + 1

      if target < nums[mid]:
        r = mid - 1
      else:
        l = mid

    return l if nums[l] == target else -1


print("======searchRange=========")
nums = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9]
target = 5
print("nums: ", nums)
print("target: ", target)
s = Solution()
res = s.searchRange(nums, target)
print("result: ", res)

print("======findLeftmost=========")
print("result:", s.findLeftmost(nums, target))

print("======findRightmost=========")
print("result:", s.findRightmost(nums, target))



