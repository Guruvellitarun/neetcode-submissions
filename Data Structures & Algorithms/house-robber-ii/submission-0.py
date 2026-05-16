class Solution:
    def rob(self, nums: List[int]) -> int:
        # we can solve this problem by partation into 2 ways
        # first partation(leave last value)
        if len(nums) <= 2:
            return max(nums)
        t0, t1 = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)-1):
            res = max(t1, t0+nums[i])
            t0 = t1
            t1 = res
        
        t2, t3 = nums[1], max(nums[1], nums[2])
        for i in range(3, len(nums)):
            res = max(t3, t2+nums[i])
            t2 = t3
            t3 = res
        
        return max(t1, t3)