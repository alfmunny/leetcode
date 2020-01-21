# 1. Hash table with two passes
class Solution1(object):
  def twoSum(self, nums, target):
    h = {}
    for i, num in enumerate(nums):
      h[num] = i

    for i, num in enumerate(nums):
      complement = target - num
      if complement in h and h[complement] != i:
        return [i, h[complement]]

# 2. Hash table with one pass
class Solution2(object):
    def twoSum(self, nums, target):
        h = {}
        for i, num in enumerate(nums):
            n = target - num

            if n not in h:
                h[num] = i
            else:
                return [h[n], i]


