class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # just think to use 2 pointers
        left = 0
        right = len(numbers)-1
        while left <= right:
            count = numbers[left] + numbers[right]
            if count == target:
                return [left+1, right+1]
            elif count >= target:
                right -= 1
            else:
                left += 1

