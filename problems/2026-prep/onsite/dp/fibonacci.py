

# Classic recursion of fibonacci
def fib(n):

    if n <= 2:
        return 1
    
    return fib(n - 1) + fib(n - 2)


def fib_dp(n):

    # memoization: we can use a hashmap
    # keys will be argument n and value will be the solution to n
    def solve(n, memo = dict()):

        if (n in memo):
            return memo[n]
        
        if n <= 2:
            return 1
        
        memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
        return memo[n]
        
    return solve(n)