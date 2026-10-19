

def calculate(s: str) -> int:

    stack = []
    sign = "+"
    current_number = 0
    for i in range(len(s)):
        char = s[i]
        if char.isdigit():
            current_number = (current_number * 10) + int(char)

        if char in "+-*/" or len(s) - 1 == i:
            if sign == "+":
                stack.append(current_number)
            elif sign == "-":
                stack.append(-current_number)
            elif sign == "*":
                stack.append(stack.pop() * current_number)
            elif sign == "/":
                stack.append(int(stack.pop() / current_number))

            sign = char
            current_number = 0
    return sum(stack)


def calculator_O1(s: str) -> int:

    if not s:
        return 0

    curr_num = 0
    sign = "+"
    result = 0
    last_num = 0

    for i in range(len(s)):
        char = s[i]

        if char.isdigit():
            curr_num = (curr_num * 10) + int(char)
        
        if char in "-+/*" or len(s) - 1 == i:
            if sign == "+":
                result += last_num
                last_num = curr_num
            elif sign == "-":
                result += last_num
                last_num = -curr_num
            elif sign == "*":
                last_num = last_num * curr_num
            elif sign == '/':
                last_num = int(last_num / curr_num)

            sign = char
            curr_num = 0

    result += last_num
    return result


# with brackets but just + and - support
def calculator_with_brackets(s: str) -> int:

    result = 0
    number = 0
    sign = 1
    stack = []

    for ch in s:
        if ch.isdigit():
            number = number * 10 + int(ch)
        elif ch == "+":
            result += sign * number
            number, sign = 0, 1
        elif ch == "-":
            result += sign * number
            number, sign = 0, -1
        elif ch == "(":
            stack.append(result)
            stack.append(sign)
            result, sign = 0, 1
        elif ch == ")":
            result += sign * number
            number = 0
            result *= stack.pop()
            result += stack.pop()

    return result + sign * number



def calculate2(s: str) -> int:
    def update(op, num, stk):
        if op == '+': stk.append(num)
        elif op == '-': stk.append(-num)
        elif op == '*': stk.append(stk.pop() * num)
        elif op == '/': stk.append(int(stk.pop() / num))

    stk, num, op = [], 0, '+'
    for ch in s:
        if ch.isdigit():
            num = num * 10 + int(ch)
        elif ch in '+-*/':
            update(op, num, stk)
            num, op = 0, ch
        # spaces fall through, ignored
    update(op, num, stk)   # flush the final number
    return sum(stk)


def calculate(self, s: str) -> int:

    def update(operator, number, stack):
        if operator == '+':
            stack.append(number)
        elif operator == "-":
            stack.append(-number)
        elif operator == "*":
            stack.append(stack.pop() * number)
        elif operator == "/":
            stack.append(int(stack.pop() / number))

    def helper(it):
        stack, number, operator = [], 0, "+"
        while it:
            ch = it.pop()
            if ch.isdigit():
                number = number * 10 + int(ch)
            elif ch == "(":
                number = helper(it)
            elif ch in "+-*/":
                update(operator, number, stack)
                number = 0
                operator = ch
            elif ch == ")":
                update(operator, number, stack)
                return sum(stack)
        update(operator, number, stack)
        return sum(stack)

    return helper(list(s[::-1]))