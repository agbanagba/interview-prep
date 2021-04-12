def count_battle_ships(board):
    row_len = len(board)
    col_len = len(board[0])

    battleships = 0
    for i in range(row_len):
        for j in range(col_len):
            if board[i][j] == 'X':
                battleships += 1
                board[i][j] = "."

                if i + 1 < row_len and board[i + 1][j] == 'X':  # the battleship is vertically aligned
                    row = i
                    while row + 1 < row_len and board[row + 1][j] == 'X':
                        board[row + 1][j] = '.'
                        row += 1
                elif j + 1 < col_len and board[i][j + 1] == 'X':  # the battleship is horizontally aligned
                    col = j
                    while col + 1 < col_len and board[i][col + 1] == 'X':
                        board[i][col + 1] = '.'
                        col += 1

    return battleships


def count_battleships_eff(board):
    row_len = len(board)
    col_len = len(board[0])

    battleships = 0
    for i in range(row_len):
        for j in range(col_len):
            if board[i][j] == 'X':
                if i == row_len - 1 or board[i + 1][j] == '.':
                    if j == col_len - 1 or board[i][j + 1] == '.':
                        battleships += 1

    return battleships


if __name__ == '__main__':
    brd1 = [["X", ".", ".", "X"], [".", ".", ".", "X"], [".", ".", ".", "X"]]
    brd2 = [["."]]
    print(count_battle_ships(brd2))
