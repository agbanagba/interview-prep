

# Given a target and wordBan, return the number of ways that the target
# can be constructed by concatenating elements of the wordbank

from typing import List

def countConstruct(target:str, wordBank: List[str], memo={}) -> int:

    if target == "":
        return 1
    
    if target in memo:
        return memo[target]
    
    totalCounter = 0
    
    for word in wordBank:

        if target.startswith(word):
            slice = target[len(word):]

            numways = countConstruct(slice, wordBank, memo)
            totalCounter += numways

    memo[target] = totalCounter
    return totalCounter


if __name__ == "__main__":
    print(countConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))
    print(countConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
    print(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", [
        "e",
        "ee",
        "eee",
        "eeee",
        "eeeee",
        "eeeeeee"
    ]))
        
