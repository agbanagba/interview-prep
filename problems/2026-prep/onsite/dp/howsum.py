

def howSum(target, numbers, memo={}):

    if target in memo:
        return memo[target]
    
    if target == 0:
        return []
    
    if target < 0:
        return None
    
    for num in numbers:
        remainder = target - num
        result = howSum(remainder, numbers, memo)

        if result is not None:
            memo[target] = result + [num]
            return memo[target]
        
    memo[target] = None
    return None


def howSum_1D(target, numbers):
    
    table = [None for _ in range(target + 1)]
    table[0] = []


    for i in range(target + 1):
        if table[i] != None:
            for num in numbers:
                if i + num < len(table):
                    table[i + num] = table[i] + [num]

    return table[target]


if __name__ == "__main__":
    print(howSum_1D(7, [5, 3, 4]))