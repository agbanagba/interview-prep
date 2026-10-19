import heapq
from typing import List
from collections import deque


# This approach uses a max heap to track the max value. 
def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    heap = []
    result = []
    left = 0

    for right in range(len(nums)):
        heapq.heappush_max(heap, (nums[right], right))

        if right - left + 1 == k:
            while heap[0][1] < left:
                heapq.heappop_max(heap)

            result.append(heap[0][0])
            left += 1

    return result


# This uses a deque to remove small items from the back and expired items 
# from the front.
def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    dq = deque()         # indices, values decreasing front to back
    result = []
    left = 0

    for right in range(len(nums)):
        # drop smaller values from the back: they can never be the max again
        while dq and nums[dq[-1]] <= nums[right]:
            dq.pop()
        dq.append(right)

        if right - left + 1 == k:
            # front slid out of the window
            if dq[0] < left:
                dq.popleft()

            result.append(nums[dq[0]])
            left += 1

    return result