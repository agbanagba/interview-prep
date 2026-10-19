from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map:
            return ""
        arr = self.time_map[key]

        # Perform binary search
        left = 0
        right = len(arr)

        while left < right:
            mid = (left + right) // 2
            if arr[mid][0] <= timestamp:
                left = mid + 1
            else:
                right = mid

        return "" if right == 0 else arr[right - 1][1]

