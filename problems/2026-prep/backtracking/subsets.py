from typing import List

def subsets(nums: List[int]) -> List[List[int]]:

    result = []

    def backtrack(idx, path):

        # Base case: No base case in this approach. There is one in the HelloInterview approach
        result.append(path[:])

        for i in range(idx, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

    backtrack(0, [])
    return result