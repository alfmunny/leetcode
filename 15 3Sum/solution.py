class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        marker = {}
        res = []

        snums = sorted(nums)

        for i, a in enumerate(snums):
            if a not in marker:
                hmap = {}
                l_marker = {}
                for j, b in enumerate(snums[i+1:]):
                    complement = - a - b
                    if complement in hmap and b not in l_marker:
                        res.append([a, b, complement])
                        l_marker[b] = True
                    hmap[b] = True
                marker[a] = True
            else:
                continue

        return res
