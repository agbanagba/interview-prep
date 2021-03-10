def moving_zeros_naive(nums):
    if not nums:
        return nums

    ret = [0] * len(nums)
    index = 0
    for num in nums:
        if num != 0:
            ret[index] = num
            index += 1

    return ret


def moving_zeros_naive_b(nums):
    if not nums:
        return nums

    for i in range(len(nums)):
        j = i
        while j > 0 and nums[j - 1] == 0:
            # swap items at i and i - 1
            nums[j], nums[j - 1] = nums[j - 1], nums[j]
            j -= 1


def moving_zeros_efficient(nums):
    if not nums:
        return nums

    i = 0
    while i < len(nums) and nums[i] > 0:
        i += 1

    for j in range(i, len(nums)):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1


if __name__ == '__main__':
    nums = [1]
    moving_zeros_efficient(nums)
    print(nums)
