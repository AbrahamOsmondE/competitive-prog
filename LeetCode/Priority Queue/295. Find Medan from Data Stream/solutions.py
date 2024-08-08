# We split the array into half, top largest and bottom smallest
# using 2 heap

# When adding a number, we make the number go through both heap
# This is to ensure that the largest of the small gets put into the large heap
# Or the smallest from the large gets put into the small heap
class MedianFinder(object):

    def __init__(self):
        self.large = []
        self.small = []

    def addNum(self, num):
        if len(self.large) == len(self.small):
            heapq.heappush(self.large, -heapq.heappushpop(self.small, -num))
        else:
            heapq.heappush(self.small, -heapq.heappushpop(self.large, num))
        """
        :type num: int
        :rtype: None
        """
        

    def findMedian(self):
        if len(self.large) == len(self.small):
            return float(self.large[0] - self.small[0]) / 2
        else:
            return float(self.large[0])
        """
        :rtype: float
        """
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()