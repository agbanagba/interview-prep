

# This code uses Top-Down Dynamic Programming (Memoization) to find the 
# Longest Common Subsequence by comparing two strings character by character 
# using a recursive helper function
# if string at i and j are equal we move both forward. if not, we explore. 
# one or the other and get the max. 
# Time is O(M x N)
def longest_common_subsequenc(text1: str, text2: str) -> int:

    memo = {}
    def helper(i, j):
        if i == len(text1) or j == len(text2):
            return 0
        
        if (i, j) in memo:
            return memo[(i, j)]
        
        if text1[i] == text2[j]:
            ans = 1 + helper(i + 1, j + 1)
        else:
            ans = max(helper(i, j + 1), helper(i + 1, j))
        
        memo[(i, j)] = ans
        return ans
    
    return helper(0, 0)