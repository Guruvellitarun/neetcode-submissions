class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for index, value in enumerate(numbers):
            diff = target - value
            if diff in seen:
                return [seen[diff]+1, index+1]
            seen[value] = index 
        return []
        
        