from typing import List

def maxAreaOfIsland(grid: List[List[int]]) -> int:

    max_area = 0

    def sink_island(row, col):

        if not (0 <= row < rows and 0 <= col < cols):
            return 0

        if grid[row][col] == 0:
            return 0

        grid[row][col] = 0
        current_area = 1

        current_area += sink_island(row, col + 1)
        current_area += sink_island(row, col - 1)
        current_area += sink_island(row - 1, col)
        current_area += sink_island(row + 1, col)

        return current_area

    rows = len(grid)
    cols = len(grid[0])

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                area = sink_island(row, col)
                max_area = max(area, max_area)

    return max_area


if __name__ == "__main__":
    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]

    print(maxAreaOfIsland(grid))