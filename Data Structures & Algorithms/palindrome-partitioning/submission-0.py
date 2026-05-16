class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def valid_pal(values, left, right):
            while left < right:
                if values[left] != values[right]:
                    return False
                left, right = left+1, right-1
            return True
        
        def backtracking(pack, i):
            if i >= len(s):
                res.append(pack[:])
                return
            
            for j in range(i, len(s)):
                if valid_pal(s, i, j):
                    pack.append(s[i:j+1])
                    backtracking(pack, j+1)
                    pack.pop()
        
        backtracking([], 0)

        return res