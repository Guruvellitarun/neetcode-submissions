class MedianFinder:

    def __init__(self):
        self.minHeap = []   # for large or right values
        self.maxHeap = []   # for small or left values

    def addNum(self, num: int) -> None:
        if not self.maxHeap:
            heapq.heappush(self.maxHeap, -num)
        elif num <= -self.maxHeap[0]:
            heapq.heappush(self.maxHeap, -num)
        else:
            heapq.heappush(self.minHeap, num)

        # Balancing the heapq
        if len(self.maxHeap) > len(self.minHeap)+1:
            number = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, -number)
        elif len(self.minHeap) > len(self.maxHeap):
            number = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -number)

    def findMedian(self) -> float:
        if len(self.minHeap) == len(self.maxHeap):
            return (self.minHeap[0] + -self.maxHeap[0]) / 2
        else:
            return -self.maxHeap[0]
        
