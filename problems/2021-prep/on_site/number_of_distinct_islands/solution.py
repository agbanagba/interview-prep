def num_distinct_islands(grid):
    n_rows = len(grid)
    n_cols = len(grid[0])

    distinct_islands = set()

    for i in range(n_rows):
        for j in range(n_cols):

            if grid[i][j] == 1:
                current_island = set()
                current_island.add((0, 0))
                grid[i][j] = 0
                stack = [(i, j)]
                while stack:
                    row, col = stack.pop()

                    if row - 1 >= 0 and grid[row - 1][col] == 1:
                        stack.append((row - 1, col))
                        grid[row - 1][col] = 0
                        current_island.add((i - (row - 1), j - col))

                    if row + 1 < n_rows and grid[row + 1][col] == 1:
                        stack.append((row + 1, col))
                        grid[row + 1][col] = 0
                        current_island.add((i - (row + 1), j - col))

                    if col - 1 >= 0 and grid[row][col - 1] == 1:
                        stack.append((row, col - 1))
                        grid[row][col - 1] = 0
                        current_island.add((i - row, j - (col - 1)))

                    if col + 1 < n_cols and grid[row][col + 1] == 1:
                        stack.append((row, col + 1))
                        grid[row][col + 1] = 0
                        current_island.add((i - row, j - (col + 1)))

                distinct_islands.add(frozenset(current_island))

    return len(distinct_islands)


def num_distinct_islands_recursive_dfs(grid):
    def dfs(row, col, r_origin, c_origin, curr_island):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
            return

        if grid[row][col] == 0:
            return

        curr_island.add((row - r_origin, col - c_origin))
        grid[row][col] = 0
        dfs(row - 1, col, r_origin, c_origin, curr_island)
        dfs(row + 1, col, r_origin, c_origin, curr_island)
        dfs(row, col - 1, r_origin, c_origin, curr_island)
        dfs(row, col + 1, r_origin, c_origin, curr_island)

    n_rows = len(grid)
    n_cols = len(grid[0])

    unique_islands = set()
    for r in range(n_rows):
        for c in range(n_cols):
            island = set()
            dfs(r, c, r, c, island)
            if island:
                unique_islands.add(frozenset(island))
    return len(unique_islands)


if __name__ == '__main__':
    gr = [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]]
    gr2 = [[1, 1, 0, 1, 1], [1, 0, 0, 0, 0], [0, 0, 0, 0, 1], [1, 1, 0, 1, 1]]
    gr3 = [[0, 0, 1], [1, 0, 1], [1, 0, 1]]
    # print(num_distinct_islands(gr3))
    print(num_distinct_islands_recursive_dfs(gr2))
