from typing import List

def two_sum_hashmap(nums: List[int], target: int):

    hashmap = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in hashmap:
            return [i, hashmap.get(diff)]

        hashmap[nums[i]] = i
    return []


# This problem is quite different from the one above in the sense that we are not sending back a list
# of two locations that sum up but a boolean indicating if there is a sum present in list nums
def two_sum_two_pointer(nums: List[int], target: int) -> bool:

    left, right = 0, len(nums) - 1

    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return True

        if current_sum > target:
            right -= 1
        else:
            left += 1

    return False