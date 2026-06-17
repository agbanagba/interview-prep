
from typing import List


# Time complexity is O(N * L^2) where N is total number of words in the list and L  is the max length of a single word.
# space complexity is O(N*L) - primary because we have N words in the word-set but we are also creating a new string for each word L times. 
def longestStrChain(words: List[str]) -> int:

    word_set = set(words)
    memo = {}

    def dfs(word):
        if word in memo:
            return memo[word]
        

        max_chain = 1
        for i in range(len(words)):
            prev_word = word[:i] + word[i+1:]
            if prev_word in word_set:
                max_chain = max(max_chain, dfs(prev_word) + 1)

        memo[word] = max_chain
        return max_chain
    
    return max(dfs(word) for word in words)