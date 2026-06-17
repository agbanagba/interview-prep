

# Time complexity - O(M * N)
# Space complexity - O(M + N)
def multiply(num1: str, num2: str) -> str:
    if num1 == "0" or num2 == "0":
        return "0"
    
    result = [0] * (len(num1) + len(num2))
    for i in range(len(num1) - 1, -1, -1):
        for j in range(len(num2) - 1, -1, -1):

            p1 = i + j # Will hold carry value
            p2 = i + j + 1 # will hold place value

            product = int(num1[i]) * int(num2[j])
            total_sum = product + result[p2]

            result[p1] += total_sum // 10
            result[p2] = total_sum % 10

    # cleanup
    start = 0
    while start < len(result) and result[start] == 0:
        start += 1

    actual_items = result[start:]
    return "".join(map(str, actual_items))