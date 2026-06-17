def max_killed_enemies(grid):
    if len(grid) == 0:
        return 0

    def kill_enemies(i, j):
        enemy_count = 0
        row_ranges = [range(i - 1, -1, -1), range(i + 1, rows, 1)]
        col_ranges = [range(j - 1, -1, -1), range(j + 1, cols, 1)]

        for row_range in row_ranges:
            for r in row_range:
                if grid[r][j] == 'W':
                    break
                elif grid[r][j] == 'E':
                    enemy_count += 1

        for col_range in col_ranges:
            for c in col_range:
                if grid[i][c] == 'W':
                    break
                elif grid[i][c] == 'E':
                    enemy_count += 1

        return enemy_count

    rows = len(grid)
    cols = len(grid[0])

    max_count = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == '0':
                max_count = max(max_count, kill_enemies(row, col))

    return max_count


def max_killed_enemies_optimized(grid):
    # remember that dynamic programming is just used to remember what has been done before.
    # always think simple first
    # This optimization uses dynamic programming

    if len(grid) == 0:
        return 0

    rows = len(grid)
    cols = len(grid[0])

    max_count = 0
    row_hits = 0
    col_hits = [0] * cols

    for row in range(rows):
        for col in range(cols):

            if col == 0 or grid[row][col - 1] == 'W':
                row_hits = 0
                for k in range(col, cols):
                    if grid[row][k] == 'W':
                        break
                    elif grid[row][k] == 'E':
                        row_hits += 1

            if row == 0 or grid[row - 1][col] == 'W':
                col_hits[col] = 0
                for k in range(row, rows):
                    if grid[k][col] == 'W':
                        break
                    elif grid[k][col] == 'E':
                        col_hits[col] += 1

            if grid[row][col] == '0':
                max_count = max(max_count, row_hits + col_hits[col])

    return max_count
