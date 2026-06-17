def strobogrammatic_number_I(num: str):
    # number passed in as a string

    if not str:
        return True

    mp = {'1': '1', '0': '0', '6': '9', '9': '6', '8': '8'}

    lower = 0
    upper = len(num) - 1
    while lower <= upper:
        if num[lower] != mp.get(num[upper], None):
            return False

        lower += 1
        upper -= 1

    return True


# Time Limit Exceeded on Leetcode
def strobogrammatic_number_II_naive(n):
    lower = int('1' + "0" * (n - 1)) if n > 1 else 0
    upper = int("9" * n)

    strbg_nums = []
    mp = {'1': '1', '0': '0', '6': '9', '9': '6', '8': '8'}

    while lower <= upper:

        num = str(lower)
        l = 0
        r = len(num) - 1
        strbg = True
        while l <= r:
            if num[l] != mp.get(num[r], None):
                strbg = not strbg
                break
            l += 1
            r -= 1

        strbg_nums.append(num) if strbg else None
        lower += 1

    return strbg_nums


def strobogrammatic_number_II_efficient(n):
    pass


if __name__ == '__main__':
    print(strobogrammatic_number_II_naive(4))
