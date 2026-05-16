class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        def find_peak(l, r):
            while l < r:
                m = (l+r) // 2
                if mountainArr.get(m) < mountainArr.get(m + 1):
                    l = m + 1
                else:
                    r = m
            return l
        
        l, r = 0, mountainArr.length() - 1

        peak = find_peak(l, r)

        # we have to go to left side
        l, r = 0, peak
        while l <= r:
            m = (l + r) // 2
            value = mountainArr.get(m)
            if target == value:
                return m
            elif target < value:
                r = m - 1
            else:
                l = m + 1

        l, r = peak + 1, mountainArr.length() - 1
        while l <= r:
            m = (l + r) // 2
            value = mountainArr.get(m)
            if target == value:
                return m
            elif target < value:
                l = m + 1
            else:
                r = m - 1

        return -1