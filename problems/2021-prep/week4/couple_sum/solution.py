def couple_sum_naive(nums, target):
    for i in range(len(nums)):

        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i + 1, j + 1]

    return [0, 0]


def couple_sum_eff(nums, target):
    hmap = {}  # stores both the num and the non-zero index

    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in hmap:
            return [hmap.get(diff) + 1, i + 1]
        hmap[nums[i]] = i

    return [0, 0]


if __name__ == '__main__':
    arr = [2, 3, 7]
    print(couple_sum_eff(arr, 7))
