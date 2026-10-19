def numIslands(grid):

    if not grid:
        return 0

    ROWS, COLS = len(grid), len(grid[0])
    island_count = 0

    def sink_island(r, c):
        if (r <0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == '0'):
            return

        grid[r][c] = '0'

        sink_island(r + 1, c)
        sink_island(r, c + 1)
        sink_island(r - 1, c)
        sink_island(r, c - 1)


    island_count = 0
    for i in range(ROWS):
        for j in range(COLS):
            if grid[i][j] == '1':
                island_count += 1
                sink_island(i, j)

    return island_count