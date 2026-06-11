

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


def calculator_with_brackets(s: str) -> int:

    if not s:
        return 0
    
    current_number = 0
    sign = "+"
    