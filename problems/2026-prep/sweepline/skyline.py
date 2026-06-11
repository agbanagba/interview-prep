import heapq
from typing import List

def getSkyLine(buildings: List[List[int]]) -> List[List[int]]:
    
    if not buildings:
        return []

    events = []
    for left, right, height in buildings:
        events.add((left, -height, ('start', height, right))) # This will add a building left edge
        events.add((right, 0, ('end',)))

    events.sort()

    result = []
    heap = []  # max heap of (height, expiry)
    prev_max_height = 0

    for x, _, payload in events:
        # start events push onto the heap
        if payload[0] == 'start':
            _, height, expiry = payload
            heapq.heappush_max(heap, (height, expiry))

        while heap and heap[0][1] <= x:
            heapq.heappop_max(heap)

        # We are looking at the top of the heap if there is anything 
        # to check the current height
        current_max_height = heap[0][0] if heap else 0
        if current_max_height != prev_max_height:
            result.append([x, current_max_height])
            prev_max_height = current_max_height

    return result