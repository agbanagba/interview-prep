def restore_ip_address(s):
    def valid(segment):
        return int(segment) <= 255 if segment[0] != '0' else len(segment) == 1

    def helper(idx, rem, sol):
        if rem == 0 and len(sol) == 4:
            solution.append('.'.join(sol))
            return

        if len(sol) == 4 or rem <= 0:
            return

        for i in range(1, 4):
            val = s[idx: idx + i]
            if valid(val):
                helper(idx + i, len(s) - idx - i, sol + [val])

    solution = []
    helper(0, len(s), [])
    return solution


def restore_ip_addr(s):
    def helper(s, ans, k, temp=''):
        if k == 4 and len(s) == 0:
            ans.append(temp[:-1])
            return

        if k == 4 or len(s) == 0:
            return

        for i in range(3):
            if k > 4 or i + 1 > len(s):
                break

            if int(s[:i + 1]) > 255:
                continue

            if i != 0 and s[0] == '0':
                continue

            helper(s[i + 1:], ans, k + 1, temp + s[:i + 1] + '.')

    solution = []
    helper(s, solution, 0, '')
    return solution


if __name__ == '__main__':
    ip_add = '25525511135'
    ip_add1 = '0000'
    ip_add2 = '101992592'
    ip_add3 = '101023'
    print(restore_ip_address(ip_add1))
