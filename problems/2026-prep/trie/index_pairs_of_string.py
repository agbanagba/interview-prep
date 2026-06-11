from typing import List

def index_pairs_brute_force(text: str, words: list[str]) -> list[list[int]]:
    result = []
    for i in range(len(text)):
        for word in words:
            j = i + len(word) - 1
            if j < len(text) and text[i:j+1] == word:
                result.append([i, j])
    result.sort()  # Python's list sort is lexicographic on lists, so [i,j] sorts by i then j
    return result

class TrieNode:

    def __init__(self):
        self.children: dict[str, TrieNode] = {}
        self.is_word = False


def build_trie(words: List[str]) -> TrieNode:
    root = TrieNode()

    for word in words:
        node = root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()

            node = node.children[ch]
        node.is_word = True
    return root

def indexPairs(text:str, words: List[str]) -> List[List[str]]:
    root = build_trie(words)

    result = []
    n = len(text)

    for i in range(n):
        node = root
        for j in range(i, n):
            ch = text[j]
            if ch not in node.children:
                break
            node = node.children[ch]
            if node.is_word:
                result.append([i, j])

    result.sort()
    return result