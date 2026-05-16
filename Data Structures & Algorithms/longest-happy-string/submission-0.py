class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        maxHeap = []
        for count, value in ([-a, "a"], [-b, "b"], [-c, "c"]):
            if count != 0:
                heapq.heappush(maxHeap, [count, value])
        
        res = ''
        while maxHeap:
            count1, value1 = heapq.heappop(maxHeap)

            if len(res) >= 2 and res[-2] == res[-1] == value1:

                if not maxHeap:
                    break

                count2, value2 = heapq.heappop(maxHeap)
                res += value2
                count2 += 1

                if count2 != 0:
                    heapq.heappush(maxHeap, [count2, value2])
                heapq.heappush(maxHeap, [count1, value1])
            else:
                res += value1
                count1 += 1
                if count1 != 0:
                    heapq.heappush(maxHeap, [count1, value1])
        return res
        