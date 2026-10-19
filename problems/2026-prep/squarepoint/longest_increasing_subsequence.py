from typing import List


def lengthofLIS(nums: List[int]) -> int:

    memo = {}
    def dp(curr, prev):
        if curr == len(nums):
            return 0

        if (curr, prev) in memo:
            return memo[(curr, prev)]

        skip = dp(curr + 1, prev)
        take = 0

        if prev == -1 or nums[curr] > nums[prev]:
            take = 1 + dp(curr + 1, curr)

        ans = max(skip, take)
        memo[((curr, prev))] = ans
        return ans

    return dp(0, -1)


def lengthLIS_Recursive(nums: List[int]) -> int:

    if not nums:
        return 0

    dp = [1] * len(nums)

    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)