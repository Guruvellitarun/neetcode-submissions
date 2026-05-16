class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips = sorted(trips, key = lambda x: x[1])

        total_members = 0
        minHeap = []

        for passengers, start, end in trips:
            while minHeap and minHeap[0][0] <= start:
                out, members = heapq.heappop(minHeap)
                total_members -= members
            
            total_members += passengers
            if total_members > capacity:
                return False
            
            heapq.heappush(minHeap, (end, passengers))
        return True