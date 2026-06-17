# not a correct solution. Works if the same idx does not come again else we'll have a circular
# dependency
def rotate(nums, k):
    n = len(nums)

    i = 0
    idx = 0
    tmp = nums[idx]
    while i < n:
        ival = tmp
        new_loc = (idx + k) % n
        tmp = nums[new_loc]
        nums[new_loc] = ival
        idx = new_loc
        i += 1


# this is the correct implementation to the solution above.
def rotate_cyc(nums, k):
    n = len(nums)

    k %= n
    start = count = 0
    while count < n:
        current, prev = start, nums[start]

        while True:
            next_idx = (current + k) % n
            nums[next_idx], prev = prev, nums[next_idx]
            current = next_idx
            count += 1

            if start == current:
                break

        start += 1


def rotate_rev(nums, k):
    # reverse the whole arr
    # reverse the first k elements
    # reverse the elements from k to n

    def reverse(vals, i, j):
        while i < j:
            vals[i], vals[j] = vals[j], vals[i]
            i += 1
            j -= 1

    if len(nums) == 1:
        return

    k = k % len(nums)
    start_idx, end_idx = 0, len(nums) - 1
    reverse(nums, start_idx, end_idx)
    reverse(nums, start_idx, k - 1)
    reverse(nums, k, end_idx)


if __name__ == '__main__':
    ns = [1, 2, 3, 4, 5, 6, 7]
    ns2 = [-1, -100, 3, 99]
    ns3 = [-1]
    ns4 = [1, 2]
    rotate_rev(ns, 3)
    rotate_rev(ns2, 2)
    rotate_rev(ns3, 2)
    rotate_rev(ns4, 3)
    print(ns)
    print(ns2)
    print(ns3)
    print(ns4)
