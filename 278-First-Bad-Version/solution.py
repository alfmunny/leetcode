class Solution:
    def firstBadVersion(self, n):

        if n == 1:
            return 1

        l, r = 2, n

        while l <= r:
            mid = (l + r) // 2
            if isBadVersion(mid) and not isBadVersion(mid - 1):
                return mid
            elif isBadVersion(mid):
                r = mid - 1
            else:
                l = mid + 1
        return 1
