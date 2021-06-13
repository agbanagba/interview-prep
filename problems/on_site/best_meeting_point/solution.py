import collections
import math


# https://leetcode.com/problems/best-meeting-point/
# This solution gave a TLE in leetcode
def min_total_distance(grid):
    if not grid:
        return 0

    # first traverse the grid to know the locations of the houses
    homes = []
    min_distance = math.inf

    m = len(grid)
    n = len(grid[0])

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                homes.append((i, j))

    # now we traverse again
    for i in range(m):
        for j in range(n):
            # calculate the distance from (i, j) to all homes
            distance = 0
            for x, y in homes:
                distance += abs(j - y) + abs(i - x)
            min_distance = min(min_distance, distance)

    return min_distance


def min_total_distance_bfs(grid):
    def search(row, col):
        queue = collections.deque()
        visited = [[False] * n for _ in range(m)]
        queue.append((row, col, 0))
        total_distance = 0

        while queue:
            r, c, d = queue.popleft()
            if r < 0 or r >= m or c < 0 or c >= n or visited[r][c]:
                continue

            if grid[r][c] == 1:
                total_distance += d

            visited[r][c] = True
            queue.append((r + 1, c, d + 1))
            queue.append((r - 1, c, d + 1))
            queue.append((r, c + 1, d + 1))
            queue.append((r, c - 1, d + 1))

        return total_distance

    min_distance = math.inf
    m = len(grid)
    n = len(grid[0])

    for i in range(m):
        for j in range(n):
            distance = search(i, j)
            min_distance = min(min_distance, distance)
    return min_distance


def min_total_distance_efficient(grid):
    def min_distance_1D(points, origin):
        distance = 0
        for point in points:
            distance += abs(point - origin)
        return distance

    m = len(grid)
    n = len(grid[0])

    rows, cols = [], []
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                rows.append(i)
                cols.append(j)

    row = rows[len(rows) // 2]
    cols.sort()
    col = cols[len(cols) // 2]
    return min_distance_1D(rows, row) + min_distance_1D(cols, col)


if __name__ == '__main__':
    grd1 = [[1, 0, 0, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]
    grd2 = [[1, 0]]
    print(min_total_distance_bfs(grd1))
