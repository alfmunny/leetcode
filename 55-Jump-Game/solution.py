reach = max(i + nums[i], reach) if i <= reach

lastPos = i if i + nums[i] >= lastPos

class Solution():
    def canJump(self, nums):
        reach = 0

        for i in range(len(nums)):
            if i <= reach:
                reach = max(i + nums[i], reach)

        return reach >= len(nums) - 1

print(Solution().canJump([ 2,3,1,1,4 ]))
print(Solution().canJump([ 3,2,1,0,4 ] ))

class Solution():
    def canJump(self, nums):
        lastPos = len(nums) - 1
        for i in reversed(range(len(nums))):
            if i + nums[i] >= lastPos:
                lastPos = i

        return lastPos == 0

print(Solution().canJump([ 2,3,1,1,4 ]))
print(Solution().canJump([ 3,2,1,0,4 ] ))
