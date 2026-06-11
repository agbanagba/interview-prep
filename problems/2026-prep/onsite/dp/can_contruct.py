from typing import List
# Given a target string and an array of word bank, return a boolean
# if we can construct target from wordbank

def canConstruct(target: str, wordBank: List[str], memo={}) -> bool:

    if target in memo:
        return memo[target]
    
    if target == "":
        return True
    
    for word in wordBank:

        if target.startswith(word):
            # return False

            remainder = target[len(word):]
            if canConstruct(remainder, wordBank, memo):
                memo[target] = True
                return True
        
    memo[target] = False
    return False

if __name__ == "__main__":
    print(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
    print(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", [
        "e",
        "ee",
        "eee",
        "eeee",
        "eeeee",
        "eeeeeee"
    ]))
        
