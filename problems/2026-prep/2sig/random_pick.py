from typing import List
import random

class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sum = []
        current_sum = 0

        for weight in w:
            current_sum += weight
            self.prefix_sum.append(current_sum)

        self.total_sum = current_sum

    # Time is O(logn)
    def pickIndex(self) -> int:
        target = random.randint(1, self.total_sum)
        low, high = 0, len(self.prefix_sum) - 1

        while low < high:
            mid = (low + high) // 2
            if self.prefix_sum[mid] < target:
                low = mid + 1
            else:
                high = mid
        return low