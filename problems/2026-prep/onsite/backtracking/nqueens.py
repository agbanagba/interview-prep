from typing import List

def solveNQueens(n: int) -> List[List[str]]:

    used_cols = set()
    used_diag_pos = set()
    used_diag_neg = set()
    
    #  I want to tackle this row wise. 
    # and with the strategy of 
    def backtrack(row):

        if row == n:
            formatted_board = []
            for col in board_state:
                row_string = "." * col + "Q" + '.' * (n - col - 1)
                formatted_board.append(row_string)
            result.append(formatted_board)
            return

        # Ideal
        for col in range(n):

            # is queen safe property. This will be based on where the queen is on the prev row. 
            if col in used_cols or (row + col) in used_diag_pos or (row - col) in used_diag_neg:
                continue

            used_cols.add(col)
            used_diag_pos.add(row + col)
            used_diag_neg.add(row - col)
            board_state.append(col)
            backtrack(row + 1)

            used_cols.remove(col)
            used_diag_pos.remove(row + col)
            used_diag_neg.remove(row - col)
            board_state.pop()
        
    board_state = []
    result = []
    backtrack(0)
    return result

def nQueens(n):

    result = []
    board = [['.' for _ in range(n)] for _ in range(n)]

    def is_valid(row, col):

        # check column above
        for i in range(row):
            if board[i][col] == 'Q':
                return False
            
        # check upper-left diagonal
        i = row - 1, j = col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1

        i = row - 1, j = col + 1
        while i >= 0 and j < n:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1

    def backtrack(row):
        if row == n:
            # we dump the whole board as a solution
            result.append([''.join(r) for r in board])
            return 
        
        for col in range(n):
            if is_valid(row, col):
                board[row][col] = 'Q'
                backtrack(row + 1)
                board[row][col] = '.'

    backtrack(0)
    return result


# For N-Queens II, you just return the length of the result 