# tried my best but this solution does not work with all cases.
def spiral_order(matrix):
    if not matrix: return []

    result = []
    m = len(matrix)
    n = len(matrix[0])

    # in a case of m == 1, then that loop will not run

    i, j = (0, 0)
    start = (0, 0)
    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for _ in range(max(m - 1, 1)):
        di = 0
        # n_vals = (m * n) - (n - 2) if m != 1 or n != 1 else 1
        n_vals = (m * n) - (n - 2) if m != 1 else n
        for p in range(n_vals):
            # we want to keep moving i and j with respect to the m, n and start boundaries.
            # remember we are using start as our start position
            result.append(matrix[i + start[0]][j + start[1]])

            # now we want to update i and j for next iteration
            tmp_i, tmp_j = i + direction[di][0], j + direction[di][1]
            if 0 <= tmp_i < m and 0 <= tmp_j < n:
                i, j = tmp_i, tmp_j
            else:
                # calculate a new direction and go there
                di = (di + 1) % 4
                i, j = i + direction[di][0], j + direction[di][1]

        m -= 2
        n -= 2
        start = (i + 1, j + 1)
    return result


def sprial_order_works(matrix):
    if not matrix: return []

    m, n = (len(matrix), len(matrix[0]))
    seen = [[False] * n for _ in matrix]
    result = []

    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    i = j = di = 0
    for _ in range(m * n):

        result.append(matrix[i][j])
        seen[i][j] = True
        tmp_i, tmp_j = i + direction[di][0], j + direction[di][1]
        if 0 <= tmp_i < m and 0 <= tmp_j < n and not seen[tmp_i][tmp_j]:
            i, j = tmp_i, tmp_j
        else:
            # calculate a new direction and go there
            di = (di + 1) % 4
            i, j = i + direction[di][0], j + direction[di][1]
    return result


if __name__ == '__main__':
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    mat2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    mat3 = [[1]]
    mat4 = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24],
            [25, 26, 27, 28, 29, 30]]
    print(sprial_order_works(mat4))
