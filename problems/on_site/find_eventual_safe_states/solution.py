def eventual_safe_nodes(graph):
    pass


if __name__ == '__main__':
    gph = [[1, 2], [2, 3], [5], [0], [5], [], []]
    gph2 = [[1, 2, 3, 4], [1, 2], [3, 4], [0, 4], []]

    print(eventual_safe_nodes(gph))
    print(eventual_safe_nodes(gph2))
