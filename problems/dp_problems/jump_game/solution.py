def can_jump(nums):
    def jump(idx, memo={}):
        if idx in memo:
            return memo[idx]

        if idx == len(nums) - 1:
            return True

        if idx > len(nums) - 1:
            return False

        for i in range(1, nums[idx] + 1):
            if jump(idx + i, memo):
                memo[idx] = True
                return memo[idx]

        memo[idx] = False
        return False

    return jump(0)


def can_jump_greedy(nums):
    good_idx = len(nums) - 1
    for i in range(len(nums) - 2, -1, -1):
        if i + nums[i] >= good_idx:
            good_idx = i

    return good_idx == 0


if __name__ == '__main__':
    ns = [2, 3, 1, 1, 4]
    ns2 = [3, 2, 1, 0, 4]
    ns3 = [0, 3, 0]
    print(can_jump_greedy(ns))
