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

def subsetsWithDup(nums: List[int]) -> List[List[int]]:
    
    nums.sort()
    def backtrack(start_idx, path):
        subsets.append(path[:])

        for i in range(start_idx, len(nums)):

            if i > start_idx and nums[i] == nums[i - 1]:
                continue

            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()
        
    subsets = []
    backtrack(0, [])
    return subsets