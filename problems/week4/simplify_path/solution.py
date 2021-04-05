def simplify_path(path):
    # rules:
    # guaranteed that all paths will start with a /
    # 1. . ignore and move to the next
    # 2. .. remove the previous dir i.e pop from the stack
    # 3. replace // with /
    # 4. remove trailing / if exists

    stack = []
    path = path.split('/')  # we'll have empty strings in place of / so we ignore.

    for item in path:

        # Ignore spaces. We want to pass so we do nothing.
        if item == '.' or item == '':
            continue

        if item == '..':
            if stack:
                stack.pop()
        else:
            stack.append(item)

    return '/' + '/'.join(stack)


if __name__ == '__main__':
    path = '/../'
    print(simplify_path(path))
