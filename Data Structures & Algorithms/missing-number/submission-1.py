class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # n = len(nums)
        # res = 0
        # for i in range(n):
        #     res ^= i
        #     res ^= nums[i]
        # res ^= n
        # return res
        count = 0
        for i in range(1, len(nums)+1):
            count += i
        return count - sum(nums)