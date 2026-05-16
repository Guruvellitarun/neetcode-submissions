class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def canSplit(largest):
            currSum = 0
            subArrays = 1
            for n in nums:
                currSum += n
                if currSum > largest:
                    subArrays += 1
                    if subArrays > k:
                        return False
                    currSum = n
            return True

        l, r = max(nums), sum(nums)
        res = r
        while l <= r:
            m = (l + r) // 2
            if canSplit(m):
                res = m
                r = m - 1
            else:
                l = l + 1
        return res