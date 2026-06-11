from typing import List

import heapq

def mergeKLists(lists) -> List[int]:

    if not lists:
        return None

    heads = [head for head in lists if head]

    dummy = ListNode(0)
    current = dummy
    heap = []
    for head in heads:
        heapq.heappush(heap, (head.val, id(head), head))

    while heap:
        val, _, node = heapq.heappop(heap)
        current.next = node
        current = current.next

        if node.next:
            heapq.heappush(heap, (node.next.val, id(node.next), node.next))

    return dummy.next