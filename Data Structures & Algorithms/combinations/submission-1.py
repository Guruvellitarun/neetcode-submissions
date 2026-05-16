class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        if n == 1:
            return [[1]]
        def backtracking(i, curr, lenght):
            if lenght == k:
                res.append(curr[:])
                return
            
            if lenght > k or i > n:
                return
            
            curr.append(i)
            backtracking(i+1, curr, lenght+1)
            curr.pop()
            backtracking(i+1, curr, lenght)
        
        backtracking(1, [], 0)

        return res