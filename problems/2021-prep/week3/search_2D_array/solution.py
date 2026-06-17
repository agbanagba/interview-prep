def linear_search(matrix, target):
    if not matrix:
        return False

    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            if target == matrix[i][j]:
                return True

    return False


def bin_search(matrix, target):
    if not matrix:
        return False

    # we want to represent the matrix as a 1d array and resolve values into i and j
    n = len(matrix)
    m = len(matrix[0])
    left = 0
    right = (m * n) - 1

    while left <= right:
        mid = left + (right - left) // 2

        # convert mid into i and j values
        i = mid // m
        j = mid % m

        if matrix[i][j] == target:
            return True

        if matrix[i][j] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False

