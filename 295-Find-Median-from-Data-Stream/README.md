# 295 - Find Median from Data Stream

[leetcode](https://leetcode.com/problems/find-median-from-data-stream/)

## Problem

    Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.
    
    For example,
    [2,3,4], the median is 3
    
    [2,3], the median is (2 + 3) / 2 = 2.5
    
    Design a data structure that supports the following two operations:
    
    void addNum(int num) - Add a integer number from the data stream to the data structure.
    double findMedian() - Return the median of all elements so far.
     
    
    Example:
    
    addNum(1)
    addNum(2)
    findMedian() -> 1.5
    addNum(3) 
    findMedian() -> 2
     
    
    Follow up:
    
    If all integer numbers from the stream are between 0 and 100, how would you optimize it?
    If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?

## Solution

```python
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
```
