from typing import List

def permutations(nums: List[int]) -> List[List[int]]:

    def backtrack(path):
        if len(path) == len(nums):
            perms.append(path[:])
            return 
        
        for num in nums:
            if num in path:
                continue

            path.append(num)
            backtrack(path)
            path.pop()

    perms = []
    backtrack([])
    return perms

# We cannot use the simple if num in paths concept because:
# 1. We don't want to reuse a number within a specific path
# 2. We don't want horizontal dups. 
# So we need a used array that turns off and on as we go down a path. 
def permutationII(nums: List[int]) -> List[List[int]]:
        nums.sort()
        used = [False] * len(nums)

        def backtrack(path):
            if len(path) == len(nums):
                perms.append(path[:])
                return

            for i in range(len(nums)):
                num = nums[i]
                if used[i] == True:
                    continue

                if i > 0 and nums[i] == nums[i - 1] and used[i - 1] == False:
                    continue

                path.append(num)
                used[i] = True

                backtrack(path)

                used[i] = False
                path.pop()

        perms = []
        backtrack([])
        return perms


def permutationsIII(nn: int) -> List[List[int]]:
    
    both_odd = lambda x, y : x % 2 != 0 and y % 2 != 0
    both_even = lambda x, y : x % 2 == 0 and y % 2 == 0

    nums = [i for i in range(1, nn + 1)]
    
    def backtrack(path):
        if len(path) == len(nums):
            perms.append(path[:])
            return

        prev_num = path[-1] if path else None

        for num in nums:
            if num in path:
                continue

            if prev_num and (both_odd(num, prev_num) or both_even(num, prev_num)):
                return

            path.append(num)
            backtrack(path)
            path.pop()

    perms = []
    backtrack([])
    return perms
    

if __name__ == "__main__":
    ns = [1,2,3,4]
    perms = permutationsIII(4)
    print(perms)