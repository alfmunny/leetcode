class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        starts = sorted([[a[0], i] for i, a in enumerate(intervals)]) + [[float('inf'), -1]]
        return [starts[bisect.bisect(starts, [x[1]])][1] for x in intervals]
