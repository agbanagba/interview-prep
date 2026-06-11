from collections import deque

from typing import List
import heapq


def highestRankedKItems(grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:

        directions = [(0, 1), (1, 0), (0 , -1), (-1, 0)]

        visited = set()
        row, col = start
        queue = deque([(0, grid[row][col], row, col)])
        visited.add((row, col))

        heap = []

        while queue:
            distance, price, row, col = queue.popleft()

            if pricing[0] <= price <= pricing[1]:
                heapq.heappush(heap, (distance, price, row, col))

            for dr, dc in directions:
                n_row = row + dr
                m_col = col + dc

                if 0 <= n_row < len(grid) and 0 <= m_col < len(grid[0]) \
                    and (n_row, m_col) not in visited \
                    and grid[n_row][m_col] != 0:
                    visited.add((n_row, m_col))
                    queue.append((distance + 1, grid[n_row][m_col], n_row, m_col))

        return [[row, col] for _, _, row, col in heapq.nsmallest(k, heap)]


if __name__ == "__main__":
    grid = [[0, 2, 0]]
    pricing = [2,2]
    start = [0, 1]
    k = 1

    result = highestRankedKItems(grid, pricing, start, k)
    print(result)