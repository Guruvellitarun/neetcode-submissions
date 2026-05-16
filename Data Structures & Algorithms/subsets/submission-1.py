class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, opt = [], []
        n = len(nums)

        def backtracking(i):
            if i == n:
                res.append(opt[:])
                return
            
            # we will not choose the num
            backtracking(i+1)

            # we will choose the number
            opt.append(nums[i])
            backtracking(i+1)
            opt.pop()

        backtracking(0)
        return res