# LC 713

from typing import List

def numSubarrayProductLessThanK(nums: List[int], k: int) -> int:

    if k <= 1:
        return 0

    left = 0
    product = 1
    total_subarrays = 0

    for right in range(len(nums)):
        product *= nums[right]

        while product >= k:
            product //= nums[left]
            left += 1

        total_subarrays += right - left + 1

    return total_subarrays
