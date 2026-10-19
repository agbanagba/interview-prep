from typing import List

def findTargetSumWays(nums: List[int], target: int) -> int:

    memo = {}

    def backtrack(idx: int, total: int):
        if idx == len(nums):
            if total == target:
                return 1
            else:
                return 0
            
        if (idx, total) in memo:
            return memo[(idx, total)]
        
        add_ways = backtrack(idx + 1, total - nums[idx])
        remove_ways = backtrack(idx + 1, total + nums[idx])

        total_ways = add_ways + remove_ways

        memo[(idx, total)] = total
        return total_ways

    return backtrack(0, 0)