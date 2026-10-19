from functools import cache


def maximumSum(self, arr: list[int]) -> int:
    
    @cache
    def dfs(i, has_deleted):
        # Base case: If we go out of bounds, return negative infinity 
        # so this path is mathematically guaranteed to lose the max() comparison.
        if i < 0:
            return -float('inf')
        
        if not has_deleted:
            # Choices: Start a new chain here, OR extend the pristine chain
            return max(arr[i], arr[i] + dfs(i - 1, False))
        
        else:
            # Choices: Extend an already-altered chain, OR delete arr[i] right now
            return max(arr[i] + dfs(i - 1, True), dfs(i - 1, False))

    # The DFS only finds the max chain ENDING at a specific index.
    # The winning subarray could end anywhere in the middle of the array,
    # so we must check every possible ending index to find the global high score.
    global_max = -float('inf')
    for i in range(len(arr)):
        global_max = max(global_max, dfs(i, False), dfs(i, True))
        
    return global_max

def maximumSum(arr: list[int]) -> int:
    # Base case: if there's only one number, you can't delete it (subarray must have at least 1 element)
    if len(arr) == 1:
        return arr[0]

    # 1. Initialize the timelines at the very first number (Index 0)
    pristine = arr[0]  # Max sum ending here with NO deletions
    altered = 0        # Max sum ending here WITH 1 deletion (0 for now)
    global_max = arr[0]

    # 2. Walk through the rest of the array starting at Index 1
    for i in range(1, len(arr)):
        num = arr[i]

        # 3. Update the Altered Timeline FIRST 
        # Choice A: We already deleted a number in the past -> (altered + num)
        # Choice B: We delete THIS number right now -> (previous pristine)
        altered = max(altered + num, pristine)

        # 4. Update the Pristine Timeline
        # Choice A: Extend the ongoing chain -> (pristine + num)
        # Choice B: The old chain is terrible, start a new one here -> (num)
        pristine = max(pristine + num, num)

        # 5. Update our global high score
        global_max = max(global_max, pristine, altered)

    return global_max