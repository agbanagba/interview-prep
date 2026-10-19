

# Classic recursion of fibonacci
def fib(n):

    if n <= 2:
        return 1
    
    return fib(n - 1) + fib(n - 2)


def fib_dp(n):

    # memoization: we can use a hashmap
    # keys will be argument n and value will be the solution to n
    memo = {}
    def solve(n):

        if n in memo:
            return memo[n]
        
        if n <= 2:
            return 1
        
        memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
        return memo[n]
        
    return solve(n)


def fib_iterative(n):

    table = [0 for _ in range(n + 1)]
    table[1] = 1

    for i in range(n):
        table[i + 1] += table[i]
        if i < n - 1:
            table[i + 2] += table[i]

    return table[n]


if __name__ == "__main__":
    print(fib_iterative(50))