from typing import List

def isValidSudoku(board: List[List[str]]) -> bool:

    col_sets = [set() for i in range(len(board))]
    row_sets = [set() for _ in range(len(board))]

    box_sets = [set() for _ in range(len(board))]

    for i in range(len(board)):
        for j in range(len(board)):

            val_ij = board[i][j]
            if val_ij == '.':
                continue

            box_index = (i // 3) * 3 + (j // 3)
            if val_ij in box_sets[box_index]:
                return False

            if val_ij in col_sets[j]:
                return False

            if val_ij in row_sets[i]:
                return False

            box_sets[box_index].add(val_ij)
            col_sets[j].add(val_ij)
            row_sets[i].add(val_ij)

    return True