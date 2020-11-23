class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        heappush(self.small, -heappushpop(self.large, num))
        if len(self.large) < len(self.small):
            heappush(self.large, -heappop(self.small))
        

    def findMedian(self) -> float:
        if not self.large:
            return 0
        if len(self.large) > len(self.small):
            return self.large[0]
        return (self.large[0] - self.small[0]) / 2
