class Solution:
    def reorganizeString(self, s: str) -> str:
        words = Counter(s)
        maxHeap = [[-cunt, value] for value, cunt in words.items()]
        heapq.heapify(maxHeap)

        res = ""
        prev = None

        while maxHeap or prev:
            if not maxHeap and prev:
                return ""
            
            cunt, value = heapq.heappop(maxHeap)
            res += value
            cunt += 1

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None

            if cunt != 0:
                prev = [cunt, value]

        return res