
from typing import List

def combinationSum(candidates: List[int], target: int) -> List[int]:
    
    def backtrack(idx, path, remainder):

        if remainder < 0:
            return
        
        if remainder == 0:
            result.append(path[:])
            return

        for i in range(idx, len(candidates)):
            path.append(candidates[i])
            backtrack(i, path, remainder-candidates[i])
            path.pop()


    result = []
    backtrack(0, [], target)
    return result


if __name__ == "__main__":
    candidates = [2, 3, 6, 7]
    target = 7
    res = combinationSum(candidates, target)
    print(res)