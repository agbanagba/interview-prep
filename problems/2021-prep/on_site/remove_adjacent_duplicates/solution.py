def remove_duplicates_I(s):
    # using a stack here

    stack = []

    for item in s:

        # compare item with what last item in the stack
        if stack and item == stack[-1]:
            stack.pop()
        else:
            stack.append(item)

    return ''.join(stack)


# This works but results in TLE in leetcode. Oh well. It's a O(n^2), O(n) solution.
def remove_duplicates_II(s, k):
    output = []
    n = k - 1
    for item in s:
        # if output and last k items are the same with item then pop last 3 items
        if output and len(output) >= n and [item] * n == output[-n:]:
            del output[-n:]
        else:
            output.append(item)

    return ''.join(output)


def remove_duplicates_II_efficient(s, k):
    stack_counter = []

    i = 0
    while i < len(s):
        # for i in range(len(s)):
        if i == 0 or s[i] != s[i - 1]:
            stack_counter.append(1)
        else:
            inc = stack_counter.pop() + 1
            if inc == k:
                s = s.replace(s[i - k + 1:i + 1], '')
                i = i - k
            else:
                stack_counter.append(inc)
        i += 1

    return s


if __name__ == '__main__':
    s1 = "abbaca"
    s2 = "azxxzy"
    print(remove_duplicates_I(s2))

    s1 = "deeedbbcccbdaa"
    s2 = "pbbcggttciiippooaais"
    s3 = "abcd"
    print(remove_duplicates_II_efficient(s1, 3))
