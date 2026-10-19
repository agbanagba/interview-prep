from typing import List

#  here we are using a two pointer solution to determine the max area
# Using a two pointer solution generally helps because when we calculate or check, we want to move either left or right pointer
# and that movement is based on some invariant (some condition). here, it is the shorter wall. Since we are moving inwards, moving the side with the 
# taller wall means reducing the area which we don't want. We want to eliminate pairs that will not give us the max. so moving inwards the side with the 
# shorter wall gives us a chance to arrive at a max. 
# This may also be considered the greedy solution.
def solve(heights: List[int]):

    left, right = 0, len(heights) - 1

    max_area = 0

    while left < right:
        current_width = right - left
        current_height = min(heights[left], heights[right])
        current_max = current_height * current_width

        max_area = max(max_area, current_max)

        if heights[left] > heights[right]:
            right -= 1
        else:
            left += 1
    return max_area