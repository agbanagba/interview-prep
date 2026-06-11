import heapq

def topklargest(nums):

    heap = nums[:3]
    heapq.heapify(heap)

    for num in nums:
        if num > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, num)

    return heap