def set_zeros(matrix):
    visited_rows = []
    visited_cols = []

    m = len(matrix)
    n = len(matrix[0])

    for i in range(m):
        for j in range(n):
            # index every element with something to mark the original value.
            # (original, changing)
            val = matrix[i][j]
            matrix[i][j] = (val, val)

    for i in range(m):
        for j in range(n):

            if matrix[i][j][0] == 0:
                if i not in visited_rows:
                    for k in range(n):
                        matrix[i][k] = (matrix[i][k][0], 0)
                    visited_rows.append(i)

                if j not in visited_cols:
                    # set the vals in col to zero
                    for k in range(m):
                        matrix[k][j] = (matrix[k][j][0], 0)
                    visited_cols.append(j)

    for i in range(m):
        for j in range(n):
            val = matrix[i][j]
            matrix[i][j] = val[1]


def set_zeros_efficient(matrix):
    visited_rows = []
    visited_cols = []
    zero_idx = []

    m = len(matrix)
    n = len(matrix[0])

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                idx = str(i) + ',' + str(j)
                zero_idx.append(idx)

    for i in range(m):
        for j in range(n):
            idx = str(i) + ',' + str(j)
            if matrix[i][j] == 0 and idx in zero_idx:
                if i not in visited_rows:
                    for k in range(n):
                        matrix[i][k] = 0
                    visited_rows.append(i)

                if j not in visited_cols:
                    # set the vals in col to zero
                    for k in range(m):
                        matrix[k][j] = 0
                    visited_cols.append(j)


def set_zeros_efficient2(matrix):
    m = len(matrix)
    n = len(matrix[0])
    rows, cols = set(), set()

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                rows.add(i)
                cols.add(j)

    for i in range(m):
        for j in range(n):
            if i in rows or j in cols:
                matrix[i][j] = 0


if __name__ == '__main__':
    mat1 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    set_zeros_efficient2(mat1)
    print(mat1)

    mat2 = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    set_zeros_efficient2(mat2)
    print(mat2)
    #
    mat3 = [[0, 1]]
    set_zeros_efficient2(mat3)
    print(mat3)
