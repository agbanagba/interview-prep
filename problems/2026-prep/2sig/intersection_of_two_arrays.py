from typing import List

# Time complexity is O(N + M), n is nums1 and m is  nums2
# space is O(min(N, M))
def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    nums1_set = set(nums1)

    result = set()
    for num in nums2:
        if num in nums1_set:
            result.add(num)

    return list(result)
