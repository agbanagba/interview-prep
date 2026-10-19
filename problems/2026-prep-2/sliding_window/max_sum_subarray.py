

def max_subarray_sum(nums, k):

    max_sum = float('-inf')
    start = 0
    state = 0

    for end in range(len(nums)):
        state += nums[end]

        # reason we are doing +1 here is because we could have overshot
        if end - start + 1 == k:
            max_sum = max(max_sum, state)
            state -= nums[start]
            start += 1

    return max_sum


# Cleanest way I know how to write this up
def max_subarray_sum_clean(nums, k):

    window_sum = sum(nums[:k])
    max_sum = window_sum

    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum