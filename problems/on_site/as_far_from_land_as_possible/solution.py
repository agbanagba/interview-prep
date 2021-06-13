import collections


def max_distance(grid):
    n = len(grid)
    max_dist = -1
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    queue = collections.deque()
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                # also mark with another value type
                queue.append((i, j, 1))

    while queue:
        i, j, distance = queue.popleft()
        for direction in directions:
            row, col = i + direction[0], j + direction[1]
            if row < 0 or col < 0 or row >= n or col >= n or grid[row][col] != 0:
                continue

            grid[row][col] = max(grid[row][col], distance)
            max_dist = max(max_dist, distance)
            queue.append((row, col, distance + 1))

    return max_dist


if __name__ == '__main__':
    grd1 = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
    grd2 = [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
    grd3 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    print(max_distance(grd1))
