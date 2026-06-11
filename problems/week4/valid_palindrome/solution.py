def valid_palindrome(s):
    pt1, pt2 = 0, len(s) - 1
    while pt1 <= pt2:

        if s[pt1] != s[pt2]:
            return False
        pt1 += 1
        pt2 -= 1

    return True


def valid_palindrome_II(s):
    def is_palindrome(stri, low, high):

        while low < high:
            if stri[low] != stri[high]:
                return False
            low += 1
            high -= 1

        return True

    l, h = 0, len(s) - 1
    while l < h:

        if s[l] != s[h]:
            if is_palindrome(s, l + 1, h):
                return True

            if is_palindrome(s, l, h - 1):
                return True
            return False

        l += 1
        h -= 1

    return True


if __name__ == '__main__':
    s = 'aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga'
    print(valid_palindrome_II(s))
