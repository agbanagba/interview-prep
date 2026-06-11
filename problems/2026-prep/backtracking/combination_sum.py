
from typing import List

def combinationSum(candidates: List[int], target: int) -> List[List[int]]:

    result = []

    def backtrack(start_idx: int, path: List[int], target: int):

        if target == 0:
            result.append(path[:])
            return

        # To take a specific path, I have to choose from list of candidates, 
        # subtract target, appen value in path, backtrack, pop. 

        # I can return early. 
        if target < 0:
            return
        
        for i in range(start_idx, len(candidates)):
            candidate = candidates[i]
            path.append(candidate)
            backtrack(i, path, target - candidate)
            path.pop()

    backtrack(0, [], target)
    return result