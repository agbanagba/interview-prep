
from collections import deque

def num_islands(grid):

    rows = len(grid)
    cols = len(grid[0])

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    count = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '1':
                count += 1

                grid[i][j] = 0

                # Look around the neighbours until we find a '0'
                queue = deque([(i, j)])
                while queue:
                     
                    row, col = queue.popleft()

                    for d_row, d_col in directions:
                        new_row, new_col = d_row + row, d_col + col

                        if 0 <= new_row < rows and 0 <= new_col < cols:
                            if grid[new_row][new_col] == '1':
                                queue.append(queue)
                                # grid[new_row][new_col] = 0

    return count


def num_islands(grid):

    def sink_island(row, col):
        if not (0 <= row < rows and 0 <= col < cols):
            return
        
        if grid[row][col] == '0':
            return
        
        grid[row][col] = '0'

        sink_island(row + 1, col)
        sink_island(row - 1, col)
        sink_island(row, col + 1)
        sink_island(row, col - 1)


    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '1':
                count += 1
                sink_island(i, j)