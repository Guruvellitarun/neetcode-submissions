class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # here we can convert the list into the hash set 
        arr = [0] * len(nums)
        for num in nums:
            if arr[num] < 0:
                return num
            arr[num] = -1