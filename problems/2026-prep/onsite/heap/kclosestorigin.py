from typing import List

import heapq

def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

    heap = []
    for i in range(len(points)):
        x, y = points[i]
        distance = x * x + y * y

        if len(heap) < k:
            heapq.heappush(heap, (-distance, i))
        elif distance < -heap[0][0]:
            heapq.heappushpop(heap, (-distance, i))

    return [points[i] for _, i in heap]