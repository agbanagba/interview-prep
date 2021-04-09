def subarray_sum_naive(nums, k):
    count = 0
    start = 0
    while start < len(nums):

        summ = 0
        end = start
        while end < len(nums):
            summ += nums[end]
            if summ == k:
                count += 1

            end += 1

        start += 1
    return count


def subarray_sum_eff(nums, k):
    hmap, count, summ = dict(), 0, 0

    hmap[0] = 1
    for num in nums:
        summ += num
        if summ - k in hmap:
            count += hmap[summ - k]

        hmap[summ] = hmap.get(summ, 0) + 1
    return count


if __name__ == '__main__':
    arr = [1, -1, 0]
    print(subarray_sum_eff(arr, 0))
