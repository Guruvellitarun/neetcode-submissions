class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        t1, t2 = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            res = max(t2, t1+nums[i])
            t1 = t2
            t2 = res
        return res