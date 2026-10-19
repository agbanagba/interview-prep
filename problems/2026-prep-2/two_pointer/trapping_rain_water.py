from typing import List

def trappingRainWater(height: List[int]) -> int:
    if not height:
        return 0

    left, right = 0, len(height) - 1
    leftMax, rightMax = height[left], height[right]
    count = 0

    while left < right:
        if leftMax < rightMax:
            left += 1
            if height[left] >= leftMax:
                leftMax = height[left]
            else:
                count += leftMax - height[left]
        else:
            right -= 1
            if height[right] >= rightMax:
                rightMax = height[right]
            else:
                count += rightMax - height[right]

    return count