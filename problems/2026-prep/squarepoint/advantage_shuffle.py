def advantageCount(nums1: list[int], nums2: list[int]) -> list[int]:

    nums1.sort()
    rival_vals = sorted([(val, i) for i, val in enumerate(nums2)], reverse=True)

    left, right = 0, len(nums1) -1
    result = [0] * len(nums1)

    for val, idx in rival_vals:
        if nums1[right] > val:
            result[idx] = nums1[right]
            right -= 1
        else:
            result[idx] = nums1[left]
            left += 1

    return result