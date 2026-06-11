from typing import List

def exist(board: List[List[str]], word: str):

    def dfs(row, col, idx):

        if idx == len(word):
            return True

        if row < 0 or row >= rows or col < 0 or col >= cols or board[row][col] != word[idx]:
            return False

        # Choose
        temp = board[row][col]
        board[row][col] = "#"

        found = (
            dfs(row + 1, col, idx + 1) or
            dfs(row - 1, col, idx + 1) or
            dfs(row, col + 1, idx + 1) or 
            dfs(row, col - 1, idx + 1)
        )

        # UNchoose
        board[row][col] = temp
        return found



    rows, cols = len(board), len(board[0])
    for row in range(rows):
        for col in range(cols):
            if board[row][col] == word[0]:
                if dfs(row, col, 0):
                    return True

    return False