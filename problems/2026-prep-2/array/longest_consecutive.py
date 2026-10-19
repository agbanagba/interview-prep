from typing import List

# LC 128. This solution is using the sorting approach with O(nlogn) time
# and O(1) space. 
# Approach. Sort and walk the array while counting the diff. 
def longestConsecutive(nums: List[int]) -> int:
    if not nums:
        return 0

    nums.sort()

    result = 0
    streak = 0
    current_diff = 0

    for i in range(1, len(nums)):
        num = nums[i]
        diff_previous = num - nums[i - 1]

        # what do i need to do with diff_previous
        # Lets assume that's my current streak
        if current_diff != diff_previous:
            # what I just encountered is my now my current diff
            # and i reset streak. 
            current_diff = diff_previous
            streak = 0
            continue

        streak += 1

    return streak

def longestConsecutive_On(nums: List[int]) -> int:
    numSet = set(nums)
    longest = 0

    for num in numSet:
        if (num - 1) not in numSet:
            length = 1
            while (num + length) in numSet:
                length += 1

            longest = max(longest, length)

    return longest


if __name__ == "__main__":
    nums = [100, 4, 200, 1, 3, 2]
    print(longestConsecutive(nums))