def rob(nums):
    def helper(idx, memo={}):
        if idx >= len(nums):
            return 0

        if idx in memo:
            return memo[idx]

        result = 0
        memo[idx] = result
        return result

    return helper(0)
