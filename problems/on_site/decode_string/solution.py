def decode_string(s):
    stack = []
    result = ''

    for ch in s:

        # only put ch in stack if it's a string or integer
        # and ignore [. on ] pop until we find an integer

        if ch.isalnum() or ch == '[':  # in 0-9, a-zA-z
            stack.append(ch)

        if ch == ']':
            # keep popping until we find a
            part = ''
            multiplier = ''
            while 1:
                item = stack.pop()
                if item.isdigit():
                    multiplier = item + multiplier
                    if stack and stack[-1].isdigit():
                        continue
                    else:
                        break
                    # peep next item in stack. if also a digit then we need it oo. Only break if it is not

                if item.isalnum():
                    part = item + part

            part *= int(multiplier)
            # put all items in part back into the stack only if the stack is not empty
            if stack:
                stack += [item for item in part]
            else:
                result += part

    # items may be left in the stack in a case without ] as last char in the string
    return result + ''.join(stack)


if __name__ == '__main__':
    s = '3[a]2[bc]'
    s2 = '3[a2[c]]'
    s3 = '2[abc]3[cd]ef'
    s4 = 'abc3[cd]xyz'
    s5 = '10[leet]'
    s6 = '3[z]2[2[y]pq4[2[jk]e1[f]]]ef'
    # result zzz[][jkjkef]ef
    print(decode_string(s4))
