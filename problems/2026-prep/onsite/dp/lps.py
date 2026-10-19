
def longestPalindrome(s: str) -> str:

    memo = {}
    def helper(i , j):

        if i >= j:
            return True
        
        if (i, j) in memo:
            return memo[(i, j)]

        ans = False
        if s[i] == s[j]:
            # This is most likely a palindrome
            ans = helper(i + 1, j - 1)
        else:
            ans = False

        memo[(i, j)] = ans
        return ans

    best_start = 0
    best_end = 0
    max_len = 0


    for i in range(len(s)):
        for j in range(i, len(s)):
            if helper(i, j):
                current_len = j - i + 1

                if current_len > max_len:
                    max_len = current_len
                    best_start = i
                    best_end = j

    return s[best_start:best_end + 1]


def longestPalindrome_2D(s: str) -> int:

    n = len(s)
    if n == 0:
        return ""
    
    dp = [[False] * n for _ in range(n)]

    start = 0
    max_len = 1

    for i in range(n - 1, -1, -1):
        dp[i][i] = True

        for j in range(i + 1, n):
            if s[i] == s[j]:
                if j - i == 1:
                    dp[i][j] = True
                elif dp[i + 1][j - 1] == True:
                    dp[i][j] = True
            
        
            if dp[i][j] == True and j - i + 1 > max_len:
                max_len = j - i + 1
                start = i

    return s[start: start + max_len]