class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = sum_value = 0
        hashmap = {0 : 1}
        for i in nums:
            sum_value += i
            req = sum_value - k
            # if req in hashmap:
            #     result += hashmap[req]
            result += hashmap.get(req, 0)
            hashmap[sum_value] = hashmap.get(sum_value, 0)+1
        return result