import heapq
from typing import List

# the strategy here is to walk left to right, walk right to left and at each point, compute max seen so far. 
# solution is now walk left to right and at each min of the two maxes - height at that point. 
def trap(heights: List[int]) -> int:
    
    n = len(heights)
 
    # left maxes
    previous_left_max = 0
    left_maxes = [0] * n
    for i in range(n):
        previous_left_max = max(previous_left_max, heights[i])
        left_maxes[i] = previous_left_max

    right_maxes = [0] * n
    previous_right_max = 0
    for i in range(n - 1, -1, -1):
        previous_right_max = max(previous_right_max, heights[i])
        right_maxes[i] = previous_right_max

    trapped_water = 0
    for i in range(n):
        trapped_water += min(left_maxes[i], right_maxes[i]) - heights[i]

    return trapped_water

# The optimised approach for the above is a two pointer solution from left and right and working on the shorter one. 
# The idea is that if we know leftMax or rightMax is smaller, the other side would always be larger and we have the min, 
# we can just subtract the current height. 
def trap_optimized(height: List[List[int]]) -> int:

    if not height:
        return 0
    
    left = 0
    right = len(height) - 1

    left_max = 0
    right_max = 0

    trapped_water = 0

    while left < right:
        if height[left] < height[right]:
            
            # check if we need to update the left_max
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]
            left += 1

        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]
            right -= 1

    return water


# BFS + Heap
# so the idea here is to use bfs + a heap. we add all the boundary heights into the priority queue 
# then we grab the smallest and bfs with it. 
def trapII(heightMap: List[List[int]]) -> int:

    rows, cols = len(heightMap), len(heightMap[0])

    min_heap = []
    for r in range(rows):
        for c in range(cols):
            if r in [0, rows - 1] or c in [0, cols - 1]:
                heapq.heappush(min_heap, (heightMap[r][c], r, c))
                heightMap[r][c] = -1


    res = 0
    max_height = 0
    
    while min_heap:
        h, r, c = heapq.heappop(min_heap)
        max_height = max(max_height, h)
        res += max_height - h

        neighbours = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
        for nr, nc in neighbours:
            if not (0 <= nr < rows or 0 <= nc < cols or heightMap[r][c] == -1):
                continue

            heapq.heappush(min_heap, (heightMap[nr][nc], nr, nc))
            heightMap[nr][nc] = -1


    return res

if __name__ == "__main__":
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    trapped = trap(height)
    print(trapped)
