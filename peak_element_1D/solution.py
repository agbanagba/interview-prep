def find_peak(nums):
    if not nums:
        return

    l = 0
    r = len(nums) - 1
    while l < r:
        mid = (r - l) // 2
        if nums[mid + 1] > nums[mid]:
            l = mid + 1
        elif nums[mid - 1] > nums[mid]:
            r = mid
        else:
            return mid

    return l
