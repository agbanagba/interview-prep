# Example: [1, 1, 2] result = 2

#   [0, 0, 0, 0, 1, 1, 1,2, 2, 3, 3, 4]
#   [0, 1, 0, 0, 0, 1, 1, 2, 2, 3, 3, 4]
def remove_dups(nums):
    if not nums:
        return 0

    idx1 = 0
    val = nums[idx1]
    for idx2 in range(1, len(nums)):

        if nums[idx2] != val:
            val = nums[idx2]
            idx1 += 1
            nums[idx1], nums[idx2] = nums[idx2], nums[idx1]

    return idx1 + 1


def remove_dups2(nums):
    if not nums:
        return 0

    idx1, count = 1, 0
    for idx2 in range(1, len(nums)):

        if nums[idx2] == nums[idx2 - 1]:
            count += 1
        else:
            count = 0

        if count <= 1:
            nums[idx1] = nums[idx2]
            idx1 += 1

    return idx1


if __name__ == '__main__':
    ns = [0, 0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    ns2 = [1, 1, 2]

    ns3 = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4]
    print(remove_dups2(ns3))
