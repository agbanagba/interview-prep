
#  LC: 516
def longest_palindromic_subsequence(s: str) -> int:

    memo = {}
    def helper(i, j):
        if i > j:
            return 0
        
        if i == j:
            return 1
        
        if (i, j) in memo:
            return memo[(i, j)]
        
        # choice 1
        if s[i] == s[j]:
            ans = 2 + helper(i + 1, j - 1)
        else:
            ans = max(helper(i + 1, j), helper(i, j + 1))

        memo[(i, j)] = ans
        return ans
    
    return helper(0, len(s) - 1)

# LC 1682
# This will MLE on leetcode. A smart way is to convert the strings to integers and use a 3D array to story memo
def longest_palindromic_subsequenceII(s: str) -> int:

    memo = {}

    def helper(i, j, prev_char):
        if i > j:
            return 0
        
        if i == j:
            return 0
        
        if (i, j, prev_char) in memo:
            return memo[(i, j, prev_char)]
        
        
        if s[i] == s[j] and s[i] != prev_char:
            ans = 2 + helper(i + 1, j - 1, s[i])
        else:
            ans = max(helper(i, j - 1, prev_char), helper(i + 1, j, prev_char))

        memo[(i, j, prev_char)] = ans
        return ans
    
    return helper(0, len(s) - 1, "")


# Non-MLE leetcode solution
def longestPalindromeSubseq(self, s: str) -> int:
    n = len(s)
    # Map string to integers 0-25 for much faster array indexing
    nums = [ord(c) - 97 for c in s]
    
    # 3D Array instead of a dictionary! 
    # Dimensions: [n][n][27]. The 26th index represents the initial "empty" state.
    memo = [[[-1] * 27 for _ in range(n)] for _ in range(n)]

    def helper(i, j, prev_char):
        # Base Cases: 
        # i > j: Pointers crossed (even center space)
        # i == j: Pointers met on a single character (odd center space)
        # Returning 0 for BOTH guarantees our final palindrome length is even!
        if i >= j:
            return 0
        
        # Memoization array check (-1 means we haven't solved it yet)
        if memo[i][j][prev_char] != -1:
            return memo[i][j][prev_char]
        
        # Decision Tree Branch 1: Match!
        # If the outer characters match AND they aren't the illegal previous character:
        if nums[i] == nums[j] and nums[i] != prev_char:
            # Add 2 to the length, shrink the window, and update the memory!
            ans = 2 + helper(i + 1, j - 1, nums[i])
        
        # Decision Tree Branch 2: Mismatch (or illegal match)
        else:
            # We are forced to skip a character. 
            # We branch out to try skipping the left side OR the right side.
            # Crucially, because we are skipping, our prev_char memory stays exactly the same.
            ans = max(
                helper(i + 1, j, prev_char),
                helper(i, j - 1, prev_char)
            )

        memo[i][j][prev_char] = ans
        return ans
    
    # Kick off the search with pointers at the edges, 
    # and 26 as the placeholder for the initial empty state!
    return helper(0, n - 1, 26)