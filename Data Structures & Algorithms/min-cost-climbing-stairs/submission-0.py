class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) <= 2:
            return min(cost)
        t1, t2 = cost[0], cost[1]
        n = len(cost)
        total_cost = 0
        for i in range(2, n):
            total_cost = min(t2 + cost[i], t1 + cost[i])
            t1 = t2
            t2 = total_cost
        return min(t1, t2)