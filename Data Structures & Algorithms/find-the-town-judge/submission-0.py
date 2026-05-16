class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        values = defaultdict(list)
        for a, b in trust:
            values[b].append(a)
        if len(values) == 1:
            return trust[0][1]
        else:
            return -1