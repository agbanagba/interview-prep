
# Maxuimum sum of distinct subarrays with length k. LC 2461
def maximumSubarraySum(nums, k):

    num_to_index = {}
    start = 0
    max_sum = 0
    state = 0

    for end in range(len(nums)):
        current_number = nums[end]
        state += current_number
        last_occurrence = num_to_index.get(current_number, -1)

        while start <= last_occurrence or end - start + 1 > k:
            state -= nums[start]
            start += 1

        num_to_index[current_number] = end

        if end - start + 1 == k:
            max_sum = max(max_sum, state)

    return max_sum