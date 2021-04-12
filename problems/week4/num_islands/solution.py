def num_islands(grid):
    if not grid or len(grid) == 0:
        return 0

    islands = 0
    row_len = len(grid)
    col_len = len(grid[0])
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                islands += 1
                grid[i][j] = 0
                queue = [(i, j)]
                while queue:
                    # check all neighbours for 1s and keep checking until queue is empty
                    row, col = queue.pop(0)
                    if row - 1 >= 0 and grid[row - 1][col] == '1':
                        queue.append((row - 1, col))
                        grid[row - 1][col] = 0

                    if row + 1 < row_len and grid[row + 1][col] == '1':
                        queue.append((row + 1, col))
                        grid[row + 1][col] = '0'

                    if col - 1 >= 0 and grid[row][col - 1] == '1':
                        queue.append((row, col - 1))
                        grid[row][col - 1] = '0'

                    if col + 1 < col_len and grid[row][col + 1] == '1':
                        queue.append((row, col + 1))
                        grid[row][col + 1] = '0'

    return islands


def num_islands_hard(grid):
    pass


if __name__ == '__main__':
    gd = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]

    gd2 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    print(num_islands(gd2))
