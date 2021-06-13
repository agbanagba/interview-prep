import collections
import math


# https://leetcode.com/problems/shortest-distance-from-all-buildings/
# Not so good time complexity tbh but can be better.
# The approach here is to go into every empty land and bfs to every
# accessible buildings and record the distances
def shortest_distance(grid):
    def search(row, col):
        queue = collections.deque()
        queue.append((row, col, 0))

        visited = [[False] * n for _ in range(m)]
        distances = []

        while queue:
            r, c, d = queue.popleft()
            if r < 0 or r >= m or c < 0 or c >= n or visited[r][c]:
                continue

            if grid[r][c] == 1:
                distances.append(d)

            visited[r][c] = True
            if grid[r][c] not in (1, 2):
                queue.append((r + 1, c, d + 1))
                queue.append((r - 1, c, d + 1))
                queue.append((r, c + 1, d + 1))
                queue.append((r, c - 1, d + 1))

        return distances

    m = len(grid)
    n = len(grid[0])

    # I want to know how many homes we have. Don't really care
    # about their positions because we are forced to do a bfs crawl
    # around obstacles here
    no_homes, land = 0, 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                no_homes += 1
            elif grid[i][j] == 0:
                land += 1

    if land == 0: return -1

    res = []
    for i in range(m):
        for j in range(n):
            if grid[i][j] not in (1, 2):
                distance = search(i, j)
                res.append(distance)

    # Figure out if you can build a house at all.
    possible_distances = [distances for distances in res if len(distances) == no_homes]
    return -1 if not possible_distances else min([sum(distances) for distances in possible_distances])


# Here we try to bfs from a building to empty land.
def shortest_distance_efficient(grid):
    if not grid:
        return -1

    m = len(grid)
    n = len(grid[0])
    visited_num = [[0] * n for _ in range(m)]
    distances = [[0] * n for _ in range(m)]
    homes = 0

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                homes += 1
                visited = [[False] * n for _ in range(m)]
                queue = collections.deque()
                queue.append((i, j, 0))

                while queue:
                    x, y, distance = queue.popleft()
                    distances[x][y] += distance
                    visited_num[x][y] += 1

                    if x - 1 >= 0 and grid[x - 1][y] == 0 and not visited[x - 1][y]:
                        queue.append((x - 1, y, distance + 1))
                        visited[x - 1][y] = True

                    if x + 1 < m and grid[x + 1][y] == 0 and not visited[x + 1][y]:
                        queue.append((x + 1, y, distance + 1))
                        visited[x + 1][y] = True

                    if y - 1 >= 0 and grid[x][y - 1] == 0 and not visited[x][y - 1]:
                        queue.append((x, y - 1, distance + 1))
                        visited[x][y - 1] = True

                    if y + 1 < n and grid[x][y + 1] == 0 and not visited[x][y + 1]:
                        queue.append((x, y + 1, distance + 1))
                        visited[x][y + 1] = True

    result = math.inf
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 0 and visited_num[i][j] == homes and distances[i][j] < result:
                result = distances[i][j]
    return -1 if result == math.inf else result


if __name__ == '__main__':
    grd1 = [[1, 0, 2, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]
    grd2 = [[1, 0]]
    grd3 = [[1]]
    grd4 = [[1, 2, 0]]
    grd5 = [[0, 2, 1], [1, 0, 2], [0, 1, 0]]
    grd6 = [[1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1], [0, 1, 1, 0, 0, 1], [1, 0, 0, 1, 0, 1], [1, 0, 1, 0, 0, 1],
            [1, 0, 0, 0, 0, 1], [0, 1, 1, 1, 1, 0]]

    print(shortest_distance_efficient(grd1))
