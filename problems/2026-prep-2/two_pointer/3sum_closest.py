from typing import List

def threeSumClosest(nums: List[int], target: int):

    nums.sort()

    diff = float('inf')
    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1

        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if abs(target - sum) < abs(diff):
                diff = target - sum

            if sum < target:
                left += 1
            else:
                right -= 1

    return target - diff