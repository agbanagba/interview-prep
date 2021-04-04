
def min_sum_array_len(nums, target):
    import math
    min_length = math.inf
    for i in range(len(nums)):
        summ = 0
        for j in range(i, len(nums)):
            summ += nums[j]
            if summ >= target:
                min_length = min(min_length, j + 1 - i)
                break
    return 0 if min_length == math.inf else min_length


def min_sum_arry(nums, target):
    import math
    min_length = math.inf
    left = max_sum = 0

    for idx, val in enumerate(nums):

        max_sum += val
        while max_sum >= target:
            min_length = min(min_length, idx + 1 - left)
            max_sum -= nums[left]
            left += 1

    return min_length if min_length != math.inf else 0


if __name__ == '__main__':
    arr = [2, 3, 1, 2, 4, 3]
    print(min_sum_array_len(arr, 7))
