from typing import List

def minPathSum(grid: List[List[int]]) -> int:

    memo = {}
    def helper(row, col):
        if row >= rows or col >= cols:
            return 0
        
        if (row, col) in memo:
            return memo[(row, col)]
        
        if row == rows - 1 and col == cols - 1:
            return grid[row][col]
        
        ans = grid[row][col]

        ans += min(helper(row + 1, col), helper(row, col + 1))

        memo[(row, col)] = ans
        return ans
    
    rows = len(grid)
    cols = len(grid[0])

    return helper(0, 0)


if __name__ == "__name__":
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    summ = minPathSum(grid)

    print(summ)