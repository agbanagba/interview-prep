from typing import List

def solve(nums: List[int]):
    nums.sort()

    count = 0
    for i in range(len(nums) - 1, 1, -1):
        left, right = 0, i - 1
        while left < right:
            if nums[left] + nums[right] > nums[i]:
                count += right - left
                right -= 1
            else:
                left += 1

    return count