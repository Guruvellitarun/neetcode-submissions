class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        res = high

        def shipCap(cap):
            currentCap, ships = cap, 1
            for w in weights:
                if currentCap - w < 0:
                    ships += 1
                    if ships > days:
                        return False
                    currentCap = cap
                currentCap -= w
            return True

        while low <= high:
            cap = (low + high) // 2
            if shipCap(cap):
                res = min(res, cap)
                high = cap - 1
            else:
                low = cap + 1
        return res