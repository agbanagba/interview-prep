def num_decodings(s):
    def helper(idx, memo={}):

        if idx in memo:
            return memo[idx]

        if idx == len(s):
            return 1

        if s[idx] == '0':
            return 0

        if idx == len(s) - 1:
            return 1

        ans = helper(idx + 1)
        if int(s[idx:idx + 2]) <= 26:
            ans += helper(idx + 2)

        memo[idx] = ans
        return ans

    return helper(0)


if __name__ == '__main__':
    print(num_decodings('111'))
    print(num_decodings('1011'))
    print(num_decodings("0"))
