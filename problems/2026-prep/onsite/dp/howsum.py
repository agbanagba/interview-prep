

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