class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict()
        for index, value in enumerate(nums):
            count[value] = count.get(value, 0) + 1
        if k > len(count):
            return None
        i = 1
        result = []
        for key, value in sorted(count.items(), key=lambda item : item[1], reverse = True):
            if i > k:
                break
            result.append(key)
            i += 1
        return result