
class Solution(object):
	def searchRange(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[int]
		"""

		l = 0
		r = len(nums) - 1
		res = [-1, -1]

		self.searchRangeBinary(nums, target, l, r, res)

		return res

	def searchRangeBinary(self, nums, target, left, right, res):

		if (left <= right):
			mid = (left + right) // 2
			if target == nums[mid]:
				if res[0] == -1:
					res[0] = res[1] = mid
				elif mid < res[0]:
					res[0] = mid
				elif mid > res[1]:
					res[1] = mid

			self.searchRangeBinary(nums, target, left, mid - 1, res)
			self.searchRangeBinary(nums, target, mid + 1, right, res)
