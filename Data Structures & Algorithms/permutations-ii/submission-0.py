class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        def backtracking(curr, pick):
            if len(curr) == len(nums):
                res.append(curr[:])
                return
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1] and not pick[i-1]:
                    continue
                if not pick[i]:
                    curr.append(nums[i])
                    pick[i] = True
                    backtracking(curr, pick)
                    curr.pop()
                    pick[i] = False
                
        backtracking([], [False]*len(nums))
        return res