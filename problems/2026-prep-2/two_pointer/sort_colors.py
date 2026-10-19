from typing import List

def sort_colors(nums: List[int]):

    low, mid = 0, 0
    high = len(nums) - 1

    while mid <= high:

        if nums[mid] == 0:
            # swap with low as low track the right most boundary of 0s
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[high], nums[mid] = nums[mid], nums[high]
            high -= 1
        