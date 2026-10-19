from typing import List

import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists) -> List[int]:

    if not lists:
        return None

    heads = [head for head in lists if head]

    dummy = ListNode(0)
    current = dummy
    heap = []
    for idx, head in enumerate(heads):
        heapq.heappush(heap, (head.val, idx, head))

    while heap:   
        _, idx, node = heapq.heappop(heap)
        current.next = node
        current = current.next


        if node.next:
            heapq.heappush(heap, (node.next.val, idx, node.next))

    return dummy.next

# input is a list of lists of feeds where each feed is (timestamp, delta)
def merge_price_feeds(feeds):
    heap = []

    for feed_index, feed in enumerate(feeds):
        if feed:
            timestamp, delta = feed[0]
            heapq.heappush(heap, (timestamp, feed_index, 0, delta))

    current_price = 0
    result = []

    while heap:
        timestamp, feed_index, event_idx, delta = heapq.heappop(heap)
        current_price += delta
        result.append(current_price)

        next_index = event_idx + 1
        if next_index < len(feeds[feed_index]):
            next_timestamp, next_delta = feeds[feed_index][next_index]
            heapq.heappush(heap, (next_timestamp, feed_index, next_index, next_delta))

    return result