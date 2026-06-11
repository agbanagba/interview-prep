from collections import defaultdict

import heapq

def topKFrequent(nums, k):
    if not nums:
        return []
    
    mp = defaultdict(int)

    for num in nums:
        mp[num] += 1

    # now we have a map, now put it in a list of tuples
    # walk the map and get everything in a list
    items = [(freq, key) for key, freq in mp.items()]
    items.sort(reverse=True)
    
    # here I want to only return the first k most frequent. the items 
    # are already sorted by freq
    return [key for _, key in items][:k]


def topKFrequent_Heap(nums, k):
    
    if not nums:
        return []
    
    counter = defaultdict(int)
    for num in nums:
        counter[num] += 1

    heap = [(-freq, key) for key, freq in counter.items]
    heapq.heapify(heap)

    return [heapq.heappop(heap)[1] for _ in range(k) ]


def topKFrequent_HeapK(nums, k):

    if not nums:
        return []
    
    counter = defaultdict(int)
    for num in nums:
        counter[num] += 1

    heap = []
    for key, freq in counter.items():
        if len(heap) < k:
            heapq.heappush(heap, (freq, key))
        elif heap[0][0] < freq:
            heapq.heappop(heap)
            heapq.heappush(heap, (freq, key))


    return [key for _, key in heap]
