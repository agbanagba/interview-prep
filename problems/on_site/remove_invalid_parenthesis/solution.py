# For this problem, there are two possibilities per parenthesis. This looks like a DP problem
# as I'm not so sure how a DFS or BFS will solve the issue.
import collections


def remove_invalid_parenthesis(s):
    result = []

    def dp_traverse(st, idx, left_paren, right_paren, solution):
        # st: the string I'm working on
        # i: the index I'm currently on in the string
        # rem: the remaining items in the string to work on
        # left_paren: number of left parenthesis so far
        # right_paren: number of right parenthesis so far
        # solution: the valid parenthesis build so far

        # if we add char at i to the solution and the abs(left_paren - right_paren) > 1, then solution is not working
        # and we discard it

        # for terminating a solution, we can compare i to the len of the string, compare rem to 0 like we did
        # or we the addition of left paren and right paren compared to length of string
        # Anyone works but we need to revisit in order to have an efficient algorithm
        if idx == len(st):
            # TODO maybe some logic is needed here but I don't see it
            result.append(solution)
        else:
            val = st[idx]
            if val != '(' and val != ')':
                dp_traverse(st, idx + 1, left_paren, right_paren, solution + val)
            else:
                if val == '(':
                    dp_traverse(st, idx + 1, left_paren + 1, right_paren, solution + val)
                else:
                    # val here is ')' hence right paren incrementing by 1
                    dp_traverse(st, idx + 1, left_paren + 1, right_paren + 1, solution + val)

    dp_traverse(s, 0, 0, 0, "")
    return result


def remove_invalid_parenthesis_bfs(s):
    def is_valid(expr):

        count = 0
        for ch in expr:
            if ch not in ')(':
                continue

            if ch == '(':
                count += 1
            elif ch == ')':
                count -= 1

            if count < 0:
                return False
        return count == 0

    if len(s) == 0:
        return [""]

    visited = set()
    queue = collections.deque()
    queue.append(s)
    visited.add(s)

    output = []

    while queue:
        expr = queue.popleft()

        if is_valid(expr):
            output.append(expr)

        for i in range(len(expr)):
            if expr[i] not in ')(':
                continue

            candidate = expr[:i] + expr[i + 1:]
            if candidate not in visited:
                queue.append(candidate)
                visited.add(candidate)

    return output if output else [""]


if __name__ == '__main__':
    paren = "()())()"
    paren2 = "(()()"

    print(remove_invalid_parenthesis_bfs(paren))
    print(remove_invalid_parenthesis_bfs(paren2))
