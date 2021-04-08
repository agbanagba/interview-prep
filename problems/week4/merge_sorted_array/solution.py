def merge2(nums1, m, nums2, n):
    idx2 = 0
    for i in range(m, m + n):
        nums1[i] = nums2[idx2]
        idx2 += 1

    nums1.sort()


if __name__ == '__main__':
    n1 = [1, 2, 3, 4, 0, 0, 0]
    print(merge2(n1, 4, [2, 5, 6], 3))
    print(n1)
