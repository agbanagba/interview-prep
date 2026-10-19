
def minDistance(word1: str, word2: str) -> int:

    memo = {}
    def helper(i, j):

        if i == len(word1):
            return len(word2) - j
        
        if j == len(word2):
            return len(word1) - i
        
        if (i, j) in memo:
            return memo[(i, j)]
        
        if word1[i] == word2[j]:
            return helper(i + 1, j + 1)

        ans = 1
        # delete a word, replace a word(they now match), insert a new word
        ans += min(helper(i + 1, j), helper(i + 1, j + 1), helper(i, j + 1))

        memo[(i, j)] = ans
        return ans
    
    return helper(0, 0)



def minDistance_2D(word1: str, word2: str) -> int:
    pass