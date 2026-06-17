import math


def max_len_subarray_sum_naive(nums, k):
    max_len = -math.inf
    for i in range(len(nums)):
        summ = 0
        for j in range(i, len(nums)):
            summ += nums[j]

            if summ == k:
                max_len = max(max_len, j - i + 1)

    return max_len if max_len != -math.inf else 0


def max_len_subarray_sum_eff(nums, k):
    hmap, max_len, summ = dict(), -math.inf, 0

    hmap[0] = 0
    left = 0
    for i in range(len(nums)):
        summ += nums[i]
        if summ == k:
            max_len = i + 1
        else:
            if summ - k in hmap:
                max_len = max(max_len, i - hmap[summ - k])

        if summ not in hmap:
            hmap[summ] = i
    return max_len if max_len != -math.inf else 0


if __name__ == '__main__':
    ns = [5, 7, 1, 6, 4, 2, 1]
    ns2 = [1, -1, 5, -2, 3]
    ns3 = [-2, -1, 2, 1]
    print(max_len_subarray_sum_eff(ns3, 1))
