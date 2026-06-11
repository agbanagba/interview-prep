
# Given a target and wordBank, return the a 2d array of all ways that the target
# can be constructed by concatenating elements of the wordbank

from typing import List

def allConstruct(target: str, wordBank: List[str], memo={}):
    
    if target in memo:
        return memo[target]
    
    if target == "":
        return [[]]
    
    result = []
    
    for word in wordBank:
        if target.startswith(word):
            slice = target[len(word):]

            sliceWays = allConstruct(slice, wordBank, memo)
            targetWays = [[word] + way for way in sliceWays]

            result.extend(targetWays)
        
    memo[target] = result
    return result
    

if __name__ == "__main__":
    print(allConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))
    print(allConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))
    print(allConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", [
        "e",
        "ee",
        "eee",
        "eeee",
        "eeeee",
        "eeeeeee"
    ]))
