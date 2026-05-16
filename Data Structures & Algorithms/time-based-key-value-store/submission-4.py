import collections

class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:        
        if key not in self.store:
            return ''
        
        items = self.store[key]

        left = 0
        right = len(items) - 1
        res = ''

        while left <= right:
            mid = (left + right) // 2
            mid_value, mid_timestamp = items[mid]

            if mid_timestamp == timestamp:
                return mid_value
            elif mid_timestamp < timestamp:
                res = mid_value
                left = mid + 1
            else:
                right = mid - 1
        return res

