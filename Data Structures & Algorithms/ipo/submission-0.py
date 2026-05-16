class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # here we are using min and max heap
        # push the [captial, profits] into the minHeap
        # there pop all the project where captial <= current_captial
        # push them into the maxHeap
        # Check if the maxHeap is empty then break the loop
        # pop the top value of the maxHeap and add to the current_captial
        # return the captial

        minHeap = []
        maxHeap = []

        for i in range(len(capital)):
            heapq.heappush(minHeap, [capital[i], profits[i]])
        
        for _ in range(k):
            while minHeap and minHeap[0][0] <= w:
                cap, prof = heapq.heappop(minHeap)
                heapq.heappush(maxHeap, -prof)
            if not maxHeap:
                break
            w += -heapq.heappop(maxHeap)
        return w