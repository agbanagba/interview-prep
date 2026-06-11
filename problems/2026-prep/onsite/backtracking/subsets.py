from typing import List

def subsets(nums: List[int]) -> List[List[int]]:

    def dfs(idx, current_subset):

        subsets.append(current_subset[:])
        for i in range(idx, len(nums)):
            current_subset.append(nums[i])
            dfs(i + 1, current_subset)
            current_subset.pop()

    subsets = []
    dfs(0, [])
    return subsets
