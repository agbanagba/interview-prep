def update_board(board, click):
    n_rows = len(board)
    n_cols = len(board[0])
    stack = [tuple(click)]

    visited = [tuple(click)]

    if board[click[0]][click[1]] == 'M':
        board[click[0]][click[1]] = 'X'
        return

    while stack:
        row, col = stack.pop(0)
        row_col_digits = 0

        tmp_visit = []
        pos = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        for i, j in pos:
            pos_i, pos_j = row + i, col + j
            if pos_i < 0 or pos_i >= n_rows or pos_j < 0 or pos_j >= n_cols or (pos_i, pos_j) in visited:
                continue

            if board[pos_i][pos_j] == 'M':
                row_col_digits += 1
            tmp_visit.append((pos_i, pos_j))

        if row_col_digits == 0:
            visited.extend(tmp_visit)
            stack.extend(tmp_visit)
            board[row][col] = 'B'
        else:
            board[row][col] = str(row_col_digits)

    return board


if __name__ == '__main__':
    brd = [["E", "E", "E", "E", "E"], ["E", "E", "M", "E", "E"], ["E", "E", "E", "E", "E"], ["E", "E", "E", "E", "E"]]
    clk = [3, 0]

    brd2 = [["B", "1", "E", "1", "B"], ["B", "1", "M", "1", "B"], ["B", "1", "1", "1", "B"], ["B", "B", "B", "B", "B"]]
    clk2 = [1, 2]

    brd3 = [['E', 'E', 'E'], ['M', 'E', 'E']]
    update_board(brd3, [1, 2])
    print(brd3)
    # print(update_board(brd2, clk2))
