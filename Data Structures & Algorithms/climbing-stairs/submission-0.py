class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        t1, t2 = 1, 2
        for _ in range(3,n+1):
            res = t2 + t1
            t1 = t2
            t2 = res
        return t2
