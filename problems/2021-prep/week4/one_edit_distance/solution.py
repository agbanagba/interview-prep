
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
