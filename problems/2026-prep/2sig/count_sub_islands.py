
from collections import deque
from typing import List

def countSubIslands(grid1: List[List[int]], grid2: List[List[int]]) -> int:
    if not grid1 or not grid2:
        return 0

    sub_islands = 0
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    row, col = len(grid2), len(grid2[0])
    for i in range(row):
        for j in range(col):
            if grid2[i][j] == '1':
                is_sub = True

                grid2[i][j] = 0
                queue = deque([(i, j)])
                while queue:
                    r, c = queue.popleft()
                    
                    if grid1[r][c] == '0':
                        is_sub = False

                    for dir_row, dir_col in directions:
                        new_row, new_col = r + dir_row, c + dir_col

                        if 0 <= new_row < row and 0 <= new_col < col and grid2[new_row][new_col] == '1':
                            queue.append((new_row, new_col))
                            grid2[new_row][new_col] = 0

                if is_sub:
                    sub_islands += 1


    return sub_islands