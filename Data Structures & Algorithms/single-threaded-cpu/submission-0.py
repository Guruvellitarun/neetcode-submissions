class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for index, value in enumerate(tasks):
            value.append(index)
        
        tasks.sort(key = lambda x: x[0])

        res, minHeap = [], []
        currI, time = 0, 0

        while minHeap or currI < len(tasks):
            while currI < len(tasks) and time >= tasks[currI][0]:
                heapq.heappush(minHeap, [tasks[currI][1], tasks[currI][2]])
                currI += 1
            
            if not minHeap:
                time = tasks[currI][0]
            else:
                pTime, index = heapq.heappop(minHeap)
                time += pTime
                res.append(index)
        return res