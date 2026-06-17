from typing import List

class TrieNode:
    
    def __init__(self):
        self.children = {}
        self.word = None


def findWords(board: List[List[str]], words: List[str]) -> List[str]:

    # Build the trie
    root = TrieNode()
    for word in words:
        node = root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word = word

    # initiate and define dfs
    row_len, col_len = len(board), len(board[0])
    result = []

    def dfs(row, col, node):
        # check if it's out of bounds
        if row < 0 or row >= row_len or col < 0 or col >= col_len or board[row][col] not in node.children:
            return
        
        next_node = node.children[board[row][col]]
        if next_node.word:
            result.append(next_node.word)
            next_node.word = None

        temp = board[row][col]
        board[row][col] = "#"

        dfs(row + 1, col, next_node)
        dfs(row - 1, col, next_node)
        dfs(row, col + 1, next_node)
        dfs(row, col - 1, next_node)

        board[row][col] = temp

        if not next_node.children:
            del node.children[temp]

    # unlike word search I where we match with the row, col with the first
    # letter in the word, here we check everywhere. 
    for i in range(row_len):
        for j in range(col_len):
            dfs(i, j, root)

    return result