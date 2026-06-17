import collections


def walls_and_gates(rooms):
    m = len(rooms)
    n = len(rooms[0])

    for i in range(m):
        for j in range(n):
            if rooms[i][j] == 0:

                visited = [[False] * n for _ in range(m)]
                queue = collections.deque()
                queue.append((i, j, 0))

                while queue:
                    x, y, distance = queue.popleft()
                    rooms[x][y] = min(rooms[x][y], distance)

                    if x - 1 >= 0 and rooms[x - 1][y] not in (0, -1) and not visited[x - 1][y]:
                        queue.append((x - 1, y, distance + 1))
                        visited[x - 1][y] = True

                    if x + 1 < m and rooms[x + 1][y] not in (0, -1) and not visited[x + 1][y]:
                        queue.append((x + 1, y, distance + 1))
                        visited[x + 1][y] = True

                    if y - 1 >= 0 and rooms[x][y - 1] not in (0, -1) and not visited[x][y - 1]:
                        queue.append((x, y - 1, distance + 1))
                        visited[x][y - 1] = True

                    if y + 1 < n and rooms[x][y + 1] not in (0, -1) and not visited[x][y + 1]:
                        queue.append((x, y + 1, distance + 1))
                        visited[x][y + 1] = True


def walls_and_gates_1(rooms):
    if not rooms:
        return []

    m = len(rooms)
    n = len(rooms[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for i in range(m):
        for j in range(n):
            if rooms[i][j] == 0:

                queue = collections.deque()
                queue.append((i, j, 1))
                visited = [[False] * n for _ in range(m)]

                while queue:
                    x, y, distance = queue.popleft()
                    for direction in directions:
                        row, col = x + direction[0], y + direction[1]
                        if row < 0 or row >= m or col < 0 or col >= n or rooms[row][col] in (0, -1) or visited[row][col]:
                            continue

                        rooms[row][col] = min(rooms[row][col], distance)
                        visited[row][col] = True
                        queue.append((row, col, distance + 1))


def walls_and_gates_2(rooms):
    m = len(rooms)
    n = len(rooms[0])
    inf = 2147483647

    queue = collections.deque()
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for i in range(m):
        for j in range(n):
            if rooms[i][j] == 0:
                queue.append((i, j, 1))

    while queue:
        i, j, distance = queue.popleft()
        for direction in directions:
            row, col = i + direction[0], j + direction[1]
            if row < 0 or col < 0 or row >= m or col >= n or rooms[row][col] != inf:
                continue

            rooms[row][col] = min(rooms[row][col], distance)
            queue.append((row, col, distance + 1))


if __name__ == '__main__':
    rms1 = [[2147483647, -1, 0, 2147483647], [2147483647, 2147483647, 2147483647, -1], [2147483647, -1, 2147483647, -1],
            [0, -1, 2147483647, 2147483647]]
    rms2 = [[2147483647]]
    rms3 = [[0]]
    walls_and_gates_2(rms1)
    print(rms1)
