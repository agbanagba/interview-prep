# Map Equivalence
# Geographical maps representing land and water forms can be stored in the form of a grid where 1 represents land and 0 represents water. In such a scenario, land equivalence is possible by comparing grids of two maps and checking if they have any matching land regions.

# There are two grids where each cell of the grids contains either 0 or 1. If two cells share a side then they are adjacent. Cells that contain 1 form a connected region (e.g. an island) if any cell of that region can be reached by moving by row or column through the adjacent cells that contain 1.

# Overlay the first grid onto the second and if a region of the first grid completely matches a region of the second grid, the regions are matched. The task is to count the total number of such matched regions in the second grid.

# Example
# Given two 3x3 grids 1 and 2:

# grid1 = [111, 100, 100]
# grid2 = [111, 100, 101]
# There are 2 land regions in the second grid: {(0,0),(0,1),(0,2),(1,0),(2,0)} and {(2,2)}.
# Regions in grid 1 cover the first land region of grid 2, but not the second land region. There is 1 matching region.

# Making a slight alteration to the above example:

# grid1 = [111, 101, 100]
# grid2 = [111, 100, 101]
# There are no matching regions. From the first grid, the 1 at position (1,2) is not matched in the second grid's larger region. The second grid position (2,2) is not matched in grid 1.

# Function Description
# Complete the function countMatchingRegions in the editor below.

# countMatchingRegions has the following parameter(s):

# string grid1[n] — an array of bit  representing the rows of map 1
# string grid2[n] — an array of bit strings representing the rows of map 2
# Returns:

# int — number of matching land regions
# Constraints
# 1 ≤ n ≤ 100
# 1 ≤ lengths of grid1[i] and grid2[i] ≤ 100
# Grid cells contain only 0 or 1
# Sample Case
# Input:

# grid1 = ['001', '011', '100']
# grid2 = ['001', '011', '101']
# Output:

# 1
# Explanation:

# The first grid forms 2 land regions: {(0,2),(1,1),(1,2)} and {(2,0)}.
# The second grid forms 2 land regions: {(0,2),(1,1),(1,2),(2,2)} and {(2,0)}.
# Only one land region matches.


# Above problem is similar but different to LC 1905: Count Sub Islands

from collections import deque
from typing import List

def map_equivalence(grid1: List[List[int]], grid2: List[List[int]]) -> int:

    if not grid1 or not grid2:
        return 0
    
    row_len, col_len = len(grid1), len(grid1[0])
    match_count = 0
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for i in range(row_len):
        for j in range(col_len):
            if grid1[i][j] == 1 or grid2[i][j] == 1:
                is_exact_match = True # mark as true until we find out otherwise. 

                if grid1[i][j] != grid2[i][j]:
                    is_exact_match = False

                grid1[i][j] = 0
                grid2[i][j] = 0

                queue = deque([(i, j)])
                while queue:
                    r, c = queue.popleft()

                    for dir_row, dir_col in directions:
                        new_row, new_col = r + dir_row, c + dir_col

                        if 0 <= new_row < row_len and 0 <= new_col < col_len and (grid1[new_row][new_col] == 1 or grid2[new_row][new_col] == 1):
                            if grid1[new_row][new_col] != grid2[new_row][new_col]:
                                is_exact_match = False

                            queue.append((new_row, new_col))
                            grid1[new_row][new_col] = 0
                            grid2[new_row][new_col] = 0

                if is_exact_match:
                    match_count += 1

    return match_count


if __name__ == "__main__":
    grid1 = [[1,1,1], [1,0,1], [1,0,0]]
    grid2 = [[1,1,1], [1,0,0], [1,0,1]]

    print(map_equivalence(grid1, grid2))