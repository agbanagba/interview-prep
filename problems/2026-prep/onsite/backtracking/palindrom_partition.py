# LC 266 and LC 267

# Naive approach can be to use backtracking to find all permutations and when we 
# see one that's a palindrome, we return True. This is good but will result in TLE on leetcode and 
# not an optimal solution.
# Optimal uses math. A palindrome contains pairs of strings and may contain a middle char. So we just have to make sure
# that it either contains <= 1 pairs after matching. 
def canPermutePalindrom(s: str) -> bool:
    unpaired_chars = set()

    for char in s:
        if char in unpaired_chars:
            unpaired_chars.remove(char)
        else:
            unpaired_chars.add(char)

    return unpaired_chars <= 1


def generatePalindromes(s: str) -> list[str]:
    # This is also a backtracking problem with a twist. It's easy to say
    # i'll use backtracking to generate all possible palindromes but that will result in TLE. 

    from collections import Counter
    counts = Counter(s) # this is a freq map of chars in s

    odd_char = ""
    half_pool = {}

    for char, freq in counts.items():
        if freq % 2 != 0:
            if odd_char:
                return []
            odd_char = char

        if freq // 2 > 0:
            half_pool[char] = freq // 2

    target_length = sum(half_pool.values())
    results = []

    def backtrack(path):
        if len(path) == target_length:
            half_string = "".join(path)
            results.append(half_string + odd_char + half_string[::-1])
            return
        
        for char in half_pool:
            if half_pool[char] > 0:
                half_pool[char] -= 1
                path.append(char)

                backtrack(path)

                path.pop()
                half_pool[char] += 1

    backtrack([])
    return results
