class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return 0
        count_dict = dict()
        for index, value in enumerate(nums):
            count_dict[value] = count_dict.get(value, 0) + 1
            if count_dict[value] >= len(nums) / 2:
                return value