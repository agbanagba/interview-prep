import heapq


def top_k_frequent(nums, k):
    map = {}
    for num in nums:
        map[num] = map.get(num, 0) + 1

    frequencies = sorted(map.items(), key=lambda x: x[1], reverse=True)[:k]
    return [num for num, freq in frequencies[:k]]


def top_k_frequent_heap(nums, k):
    map = {}
    for num in nums:
        map[num] = map.get(num, 0) + 1

    # now we have to use a heap
    heap = []
    heapq.heapify(heap)
    for key, value in map.items():
        heapq.heappush(heap, (value, key))
        if len(heap) > k:
            heapq.heappop(heap)

    return [value for key, value in heap[::-1]]


if __name__ == '__main__':
    ls = [1, 1, 1, 2, 2, 3, 4, 4, 4, 4, 4, 4, 4, 4]
    print(top_k_frequent_heap(ls, 3))
