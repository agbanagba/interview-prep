class TrieNode:
    def __init__(self, children=None, eow=False):
        if children is None:
            self.children = {}
        else:
            self.children = children
        self.is_end_of_word = eow

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        
        return node.is_end_of_word

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def delete(self, word):
        
        def _delete(node, index):
            
            if index == len(word):
                node.is_end_of_word = False
                return len(node.children) == 0
            
            char = word[index]
            child = node.children.get(char)

            if child is None:
                return False # word not found
            
            should_delete_child = _delete(child, index + 1)
            if should_delete_child:
                del node.children[char]

            return not node.is_end_of_word and len(node.children) == 0

        _delete(self.root, 0)
