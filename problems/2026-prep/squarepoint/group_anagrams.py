from typing import List
from collections import defaultdict

# Time complexity is O(N.KlogK) because of the sorting
def groupAnagrams(self, strs: List[str]) -> list[list[str]]:

    anagram_map = defaultdict(list)
    for word in strs:
        signature = "".join(sorted(word))
        anagram_map[signature].append(word)

    return list(anagram_map.values())


def groupAnagramsOptimal(strs: List[str]) -> list[list[str]]:

    anagram_map = defaultdict(list)

    for word in strs:

        count = [0] * 26
        for char in word:
            count[ord(char) - ord('a')] += 1

        signature = tuple(count)
        anagram_map[signature].append(word)

    return list(anagram_map.values())