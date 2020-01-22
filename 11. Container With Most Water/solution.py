class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        l = 0
        r = len(height) - 1
        res = 0

        while(l < r):
            h = min(height[l], height[r])
            res = max(res, (r - l) * h)

            while(height[r] <= h and l < r):
                r -= 1
            while(height[l] <= h and l < r):
                l += 1

        return res
