class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        t0, t1, t2 = 1, 1, 2
        for i in range(3, n):
            t0, t1, t2 = t1, t2, t0+t1+t2
        return t2