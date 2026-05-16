class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = [0] * 26
        for task in tasks:
            count[ord(task) - ord('A')] += 1
        
        maxF = max(count)
        maxCount = 0
        for val in count:
            maxCount += 1 if val == maxF else 0
        
        time = (maxF - 1) * (n + 1) + maxCount

        return max(len(tasks), time)