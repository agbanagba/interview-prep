# There must be one edit distance between strings so strings of the same length can't work.
# and also strings with len diff of 2 or more cannot also work.


# TODO: Make this consider replacing one character. A replacement will occur if it's
#   1. Different case 'a' vs 'A'
#   2. A replacement can only happen on the same length of strings.
def is_one_edit_distance(s, t):
    if abs(len(s) - len(t)) > 1 or s == t:
        return False

    i, j = 0, 0
    found_inequality = False

    while i < len(s) and j < len(t):

        if s[i] != t[j]:
            if found_inequality: return False
            found_inequality = True
            if len(s) < len(t):
                i -= 1
            elif len(t) < len(s):
                j -= 1
        i += 1
        j += 1
    return True


if __name__ == '__main__':
    s1, s2 = "acbbcda", 'abbdad'
    print(is_one_edit_distance(s1, s2))
