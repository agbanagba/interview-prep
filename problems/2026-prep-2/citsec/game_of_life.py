from collections import defaultdict

def gameOfLife(board: list[list[int]]) -> None:

    m = len(board)
    n = len(board[0])

    for i in range(m):
        for j in range(n):
            cell = board[i][j]

            neighbours = [(0, 1), (0, -1), (-1, 0), (1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]
            live_neighbours = 0

            for neighbour in neighbours:
                di, dj = i + neighbour[0], j + neighbour[1]
                if 0 <= di < m and 0 <= dj < n:
                    if board[di][dj] in (1, 3):
                        live_neighbours += 1

            # apply rules on neighbours
            if cell == 1:
                if live_neighbours not in (2, 3):
                    board[i][j] = 3
            elif cell == 0:
                if live_neighbours == 3:
                    board[i][j] = 2

    for i in range(m):
        for j in range(n):
            if board[i][j] == 2:
                board[i][j] = 1
            elif board[i][j] == 3:
                board[i][j] = 0

# Since dead cells are far away from live cells they will remain dead. 
# We only have to know the location of live cells
# live_cells dictionary is only tracking live cells. 
# { (1, 2): 1, (2, 2): 1, (3, 2): 1}
def gameOfLifeSparseOptimization(m: int, n: int, live_cells: dict) -> None:
    neighbour_offset = [(0, 1), (0, -1), (-1, 0), (1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]

    # find all cells that have at least one live neighbour and count how many live neighbours they have
    neighbour_counts = defaultdict(int)
    for (r, c) in live_cells:
        for dr, dc in neighbour_offset:
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n:
                neighbour_counts[(nr, nc)] += 1

    cells_to_remove = []
    cells_to_add = []

    for (r, c), count in neighbour_counts.items():
        if (r, c) in live_cells:
            if count not in (2, 3):
                cells_to_remove.append((r, c))
        else:
            if count == 3:
                cells_to_add.append((r, c))


    for (r, c) in list(live_cells.keys()):
        if (r, c) in neighbour_counts:
            cells_to_remove.append((r, c))

    for cell in cells_to_remove:
        if cell in live_cells:
            del live_cells[cell]

    for cell in cells_to_add:
        live_cells[cell] = 1


# For an infinite board - All we have to do is don't perform the boundary check during neighbour counts. 
if __name__ == "__main__":
    board = [[1,1],[1,0]]
    gameOfLife(board)
    print(board)