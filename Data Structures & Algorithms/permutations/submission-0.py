class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtracking(curr, nums, pick):
            if len(curr) == len(nums):
                res.append(curr[:])
                return
            for i in range(len(nums)):
                if not pick[i]:
                    curr.append(nums[i])
                    pick[i] = True
                    backtracking(curr, nums, pick)
                    curr.pop()
                    pick[i] = False
        backtracking([], nums, [False]*len(nums))
        return res            