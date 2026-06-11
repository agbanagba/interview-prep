from typing import List

def longestCommonPrefix(strs: List[str]) -> str:

    if not strs:
        return ""

    prefix = strs[0]
    for s in strs[1:]:

        while not s.startswith(prefix):
            prefix = prefix[:-1]

            if not prefix:
                return ""

    return prefix


# This is the length of the longest common prefix give an 
def longestCommonPrefix(arr1: List[int], arr2: List[int]) -> int:

    prefixes = set()
    for num in arr1:
        while num > 0:
            prefixes.add(num)
            num //= 10

    max_len = 0 # This is the longsest common prefix. 

    for num in arr2:
        while num > 0:
            if num in prefixes:
                max_len = max(max_len, len(str(num)))
                break
            num //= 0

    return max_len