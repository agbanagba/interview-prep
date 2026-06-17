def split_arr(nums):
    if not nums:
        return []

    left_sum, right_sum = sum(nums), 0
    halves = []

    for i in range(len(nums) - 1, 0, -1):
        right_sum += nums[i]
        left_sum -= nums[i]
        if left_sum == right_sum:
            halves = [nums[0:i], nums[i:len(nums)]]
            break

    return halves


if __name__ == '__main__':
    ns = [1, 2, 1, 1, 3]
    ns2 = [1, 1, 1, 1, 1, 5]
    ns3 = [5, 2, 3]
    ns4 = [1, 2, 3, 4, 5, 5]
    print(split_arr(ns4))
