class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in nums and nums.index(diff) != i:
                result.append(i)
                result.append(nums.index(diff))
                return sorted(result)
        return result