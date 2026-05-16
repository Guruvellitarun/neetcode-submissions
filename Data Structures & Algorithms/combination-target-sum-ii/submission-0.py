class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        res = []
        
        def backtracking(i, curr, total):
            if total == target:
                res.append(curr[:])
                return
            if total > target or i >= len(candidates):
                return
            
            curr.append(candidates[i])
            backtracking(i+1, curr, total + candidates[i])
            curr.pop()

            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            backtracking(i+1, curr, total)
        
        backtracking(0, [], 0)
        return res
        