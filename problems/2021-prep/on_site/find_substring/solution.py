def firstOccurrence(s, x):
    s_idx = 0
    x_idx = 0

    while s_idx < len(s) and x_idx < len(x):

        if s[s_idx] == x[x_idx] or x[x_idx] == '*':
            s_idx += 1
            x_idx += 1
        else:
            x_idx = 0
            s_idx += 1

    return -1 if x_idx < len(x) - 1 else s_idx - x_idx


if __name__ == '__main__':
    s1 = "aaa"
    x1 = "aaaa"

    s2 = "xabcdey"
    x2 = "ab*de"
    print(firstOccurrence(s1, x1))
