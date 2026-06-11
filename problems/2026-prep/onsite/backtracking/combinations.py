from typing import List

def combinations(n: int, k: int) -> List[List[int]]:

    nums = [num for num in range(1, n + 1)]

    def backtrack(idx, path):
        
        if len(path) == k:
            result.append(path[:])
            return
        
        for i in range(idx, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

    result = []
    backtrack(0, [])
    return result
