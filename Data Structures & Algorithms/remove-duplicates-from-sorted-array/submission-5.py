class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        # we can do swaping right
        l = 0
        for r in range(1, len(nums)):
            if nums[r] != nums[l]:
                nums[l+1] = nums[r]
                l += 1
        return l+1