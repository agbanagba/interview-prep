from typing import List

def uniquePaths(m: int, n: int) -> int:

    #  I don't have to maintain a grid in this solution. 
    memo = {}

    def dfs(i, j):

        # we have to make sure that we are within boundary
        #  we don't have to check 0 because we are moving right and down (m and n)
        if i >= m or j >= n:
            return 0
        
        if i == m - 1 and j == n - 1:
            return 1

        if (i, j) in memo:
            return memo[(i, j)]

        # Down path
        down_path = dfs(i + 1, j)
        right_path = dfs(i, j + 1)

        total_paths = down_path + right_path
        memo[(i, j)] = total_paths
        return total_paths

    return dfs(0, 0)


def uniquePathsII(obstacleGrid: List[List[int]]) -> int:

    #  I don't have to maintain a grid in this solution. 
    memo = {}
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])

    def dfs(i, j):

        # we have to make sure that we are within boundary
        #  we don't have to check 0 because we are moving right and down (m and n)
        if i >= m or j >= n:
            return 0
        
        # Check if i, j is an obstacle. 
        if obstacleGrid[i][j] == 1:
            return 0
        
        if i == m - 1 and j == n - 1:
            return 1

        if (i, j) in memo:
            return memo[(i, j)]

        # Down path
        down_path = dfs(i + 1, j)
        right_path = dfs(i, j + 1)

        total_paths = down_path + right_path
        memo[(i, j)] = total_paths
        return total_paths

    return dfs(0, 0)


def uniquePathsIII(grid: List[List[int]]) -> int:
    
    rows, cols = len(grid), len(grid[0])

    start_r, start_c = 0, 0
    empty_squares = 0

    # scan the whole thing to figure our start row and col
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                start_r, start_c = r, c
            elif grid[r][c] == 0:
                empty_squares += 1

    total_to_visit = empty_squares + 2
    
    def backtrack(r, c, visited_count):
        if grid[r][c] == 2:
            if visited_count == total_to_visit:
                return 1
            else:
                return 0
            
        temp = grid[r][c]
        grid[r][c] = 3

        paths = 0
        for dr, dc in []:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != 3 and grid[nr][nc] != -1:
                paths += backtrack(nr, nc, visited_count+1)

        grid[r][c] = temp
        return paths
    
    return backtrack(start_r, start_c, 1)