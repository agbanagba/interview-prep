def can_partition(nums):
    _, rem = divmod(sum(nums), 2)

    if rem:
        return False

    def can_partition_k(start, arr, used, k, progress_bucket_sum, target_sum):

        if k == 1:
            return True

        if progress_bucket_sum == target_sum:
            return can_partition_k(0, arr, used, k - 1, 0, target_sum)

    return can_partition_k(0, nums, [False] * len(nums), 2, 0, sum(nums) // 2)


def can_partit(nums):
    _, rem = divmod(sum(nums), 2)

    if rem:
        return False



if __name__ == '__main__':
    arr = [1, 5, 11, 5]
    print(can_partition(arr))
