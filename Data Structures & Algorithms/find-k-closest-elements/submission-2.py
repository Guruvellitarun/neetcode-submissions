class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        min_count = defaultdict(list)
        l, res = 0, 0
        for r in range(len(arr)):
            diff = abs(x - arr[r])
            res += diff
            if r-l+1 == k:
                if res not in  min_count:
                    min_count[res] = arr[l:r+1]
                res -= abs(x - arr[l])
                l += 1    
        return min_count[min(min_count)]