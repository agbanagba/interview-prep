# This solution is stupid and naive
def rob(nums):
    def helper(idx, memo={}):
        if idx >= len(nums):
            return 0

        if idx in memo:
            return memo[idx]
        result = max(nums[idx] + helper(idx + 2), helper(idx + 1))
        memo[idx] = result
        return result

    return helper(0)


if __name__ == '__main__':
    ns1 = [2, 3, 2]
    ns2 = [1, 2, 3, 1]
    ns3 = [2, 7, 9, 3, 1]
    ns4 = [2, 1, 1, 2]
    print(rob(ns4))
