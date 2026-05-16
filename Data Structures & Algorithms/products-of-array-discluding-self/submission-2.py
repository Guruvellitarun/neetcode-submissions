import numpy as np

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        arr = np.array(nums)
        for i in range(len(arr)):
            prod = np.prod(arr[:i]) * np.prod(arr[i+1:])
            result.append(prod)

        return result