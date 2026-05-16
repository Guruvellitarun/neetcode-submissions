class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # result = []
        # for i in range(len(nums)):
        #     diff = target - nums[i]
        #     if diff in nums and nums.index(diff) != i:
        #         result.append(i)
        #         result.append(nums.index(diff))
        #         return result
        # return result

        seen = {}
        for index, value in enumerate(nums):
            diff = target - value
            if diff in seen:
                return [seen[diff], index]
            seen[value] = index
        return []