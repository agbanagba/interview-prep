def can_visit_all_rooms(rooms):
    # you can enter room 0

    rm_len = len(rooms)
    visited = [False for i in range(rm_len)]
    visited[0] = True
    stack = [0]

    while stack:
        room = stack.pop()
        for key in rooms[room]:
            # only add a key if it's not been visited
            if not visited[key]:
                stack.append(key)

        visited[room] = True

    return all(visited)


if __name__ == '__main__':
    rms = [[1], [2], [3], []]
    rms2 = [[1, 3], [3, 0, 1], [2], [0]]

    print(can_visit_all_rooms(rms))
    print(can_visit_all_rooms(rms2))
