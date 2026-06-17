def max_area_island(grid):
    if grid is None or len(grid) == 0:
        return 0

    n_rows = len(grid)
    n_cols = len(grid[0])
    max_island = 0

    for i in range(n_rows):
        for j in range(n_cols):

            area = 0
            if grid[i][j] == 1:
                area += 1
                queue = [(i, j)]
                grid[i][j] = 0
                while queue:

                    row, col = queue.pop()
                    if row - 1 >= 0 and grid[row - 1][col] == 1:
                        grid[row - 1][col] = 0
                        area += 1
                        queue.append((row - 1, col))

                    if row + 1 < n_rows and grid[row + 1][col] == 1:
                        area += 1
                        grid[row + 1][col] = 0
                        queue.append((row + 1, col))

                    if col - 1 >= 0 and grid[row][col - 1] == 1:
                        area += 1
                        grid[row][col - 1] = 0
                        queue.append((row, col - 1))

                    if col + 1 < n_cols and grid[row][col + 1] == 1:
                        area += 1
                        grid[row][col + 1] = 0
                        queue.append((row, col + 1))
            max_island = max(area, max_island)

    return max_island


if __name__ == '__main__':
    gr = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
          [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
          [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    gr2 = [[0, 0, 0, 0, 0, 0, 0, 0]]
    print(max_area_island(gr2))
