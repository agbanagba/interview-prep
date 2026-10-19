
class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_word = None


def trie(words: list[str]) -> TrieNode:
    root = TrieNode()
    for word in words:
        node = root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        node.is_word = True

    return root