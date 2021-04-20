def maximal_square_brute_force(matrix):
    m = len(matrix)
    n = len(matrix[0])
    max_area = 0

    for i in range(m):
        for j in range(n):
            x, y = i, j
            while x < m and y < n:
                if all([matrix[p][q] == "1" for p in range(i, x + 1) for q in range(j, y + 1)]):
                    area = (x - i + 1) * (y - j + 1)
                    max_area = max(max_area, area)
                x += 1
                y += 1

    return max_area


def maximal_square_efficient(matrix):
    pass


if __name__ == '__main__':
    matrix1 = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"],
               ["1", "0", "0", "1", "0"]]
    matrix2 = [["1"], ["1"]]
    matrix3 = [["0", "1"], ["1", "0"]]
    matrix4 = [["0"]]

    print(maximal_square_brute_force(matrix4))
    # print(all_ones(matrix1, 1, 3, 2, 4))
