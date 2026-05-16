class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (right + left) // 2
            char = nums[mid]
            if char == target:
                return mid
            elif char > target:
                right = mid - 1
            elif char < target:
                left = mid + 1
        return left
        

        