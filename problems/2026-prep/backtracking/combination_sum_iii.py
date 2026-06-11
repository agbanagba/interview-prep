# This is like combination sum with the caveat that each number in the candidate may only be used once. 
# and the candidates can contain duplicates so we need to handle it

# The way we tackle the duplicates is by sorting so duplicates are lined up next to each other and when we want
# to check the menu, we ensure we don't do 1->1 for instance in a specific path. 
def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    result = []

    candidates.sort()

    def backtrack(start_idx: int, path: List[int], target: int):

        if target == 0:
            result.append(path[:])
            return

        if target < 0:
            return
        
        for i in range(start_idx, len(candidates)):

            if i > start_idx and candidates[i] ==  candidates[i - 1]:
                continue
            
            candidate = candidates[i]
            path.append(candidate)
            backtrack(i + 1, path, target - candidate)
            path.pop()

    backtrack(0, [], target)
    return result