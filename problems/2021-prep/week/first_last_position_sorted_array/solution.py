def search_range(nums, target):
    if not nums or len(nums) == 1:
        return [-1, -1]

    left = 0
    right = len(nums) - 1
    while left < right:
        mid = (right + left) // 2
        if nums[mid] == target:
            return [mid, mid + 1] if nums[mid + 1] == target else [mid - 1, mid]

        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid

    return [-1, -1]


if __name__ == '__main__':
    print(search_range([1, 8], 8))
