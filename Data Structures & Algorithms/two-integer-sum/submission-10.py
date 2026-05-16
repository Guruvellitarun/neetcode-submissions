class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = {}
        for index, value in enumerate(nums):
            diff = target - value
            if diff in count:
                return [count[diff], index]
            count[value] = index
