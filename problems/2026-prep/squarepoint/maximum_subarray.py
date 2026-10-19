from typing import List

def maxSubArray(nums: List[int]) -> int:

    if len(nums) == 1:
        return nums[0]

    currentMax = nums[0]
    maxsf = nums[0]

    for i in range(1, len(nums)):
        currentMax = max(nums[i], currentMax + nums[i])
        maxsf = max(currentMax, maxsf)

    return maxsf
