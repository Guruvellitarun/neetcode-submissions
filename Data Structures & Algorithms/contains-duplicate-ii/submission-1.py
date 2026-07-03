class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        values = dict()
        for index, value in enumerate(nums):
            if value in values:
                if abs(index - values[value]) <= k:
                    return True
            values[value] = index
        return False