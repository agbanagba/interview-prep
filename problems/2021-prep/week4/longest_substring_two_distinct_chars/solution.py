def length_of_longest_substring_two_distinct(s):
    idx1 = idx2 = 0
    max_len = 1

    while idx2 < len(s):
        substr = s[idx1:idx2 + 1]

        # check if substr contains two distinct chars, move idx2 else move idx1
        substr_len = len(set(substr)) # this here will increase the complexity because the
        if substr_len <= 2:
            max_len = max(max_len, len(substr))
            idx2 += 1
        else:
            idx1 += 1

    return max_len


def length_of_longest_substring_two_distinct_eff(s):
    idx1 = idx2 = 0
    max_len = 1
    mp = {}

    while idx2 < len(s):
        if len(mp) >= 3:
            mp[s[idx1]] = mp.get(s[idx1]) - 1
            if mp[s[idx1]] == 0:
                del mp[s[idx1]]
            idx1 += 1
        else:
            mp[s[idx2]] = mp.get(s[idx2], 0) + 1
            idx2 += 1

        if len(mp) <= 2:
            max_len = max(max_len, sum(mp.values()))

    return max_len


def length_of_longest_substring_k_distinct(s, k):
    idx1 = idx2 = 0
    max_len = 0
    mp = {}

    while idx2 < len(s):
        substr = s[idx1:idx2 + 1]

        # check if substr contains two distinct chars, move idx2 else move idx1
        substr_len = len(set(substr))
        if substr_len <= k:
            max_len = max(max_len, len(substr))
            idx2 += 1
        else:
            idx1 += 1

    return max_len


if __name__ == '__main__':
    s1 = "eceba"
    s2 = "ccaabbb"
    s3 = "aaaaaaa"
    s4 = "a"
    print(length_of_longest_substring_two_distinct_eff(s4))
