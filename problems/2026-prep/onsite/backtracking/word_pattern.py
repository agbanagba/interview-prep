from collections import defaultdict

def wordPattern(pattern: str, s: str) -> bool:
    
    claimed_words = set()
    mp = {}
    wordList = s.split()


    if len(pattern) != len(wordList):
        return False

    for i in range(len(pattern)):
        ch = pattern[i]
        word = wordList[i]

        if ch in mp:
            if mp[ch] != word:
                return False
        else:
            if word in claimed_words:
                return False

            mp[ch] = word
            claimed_words.add(word)

    return True


def wordPatternII(pattern: str, s: str) -> bool:

    mp = {}
    claimed_words = set()

    def backtrack(p_idx: int, s_idx: int) -> bool:

        if p_idx == len(pattern) and s_idx == len(s):
            return True

        if p_idx == len(pattern) or s_idx == len(s):
            return False

        ch = pattern[p_idx]

        if ch in mp:
            expected_word = mp[ch]
            if s.startswith(expected_word, s_idx):
                return backtrack(p_idx + 1, s_idx + len(expected_word))
            else:
                return False
        else:
            for end_idx in range(s_idx + 1, len(s) + 1):
                guessed_word = s[s_idx: end_idx]
                if guessed_word not in claimed_words:
                    mp[ch] = guessed_word
                    claimed_words.add(guessed_word)

                    if backtrack(p_idx + 1, end_idx):
                        return True

                    del mp[ch]
                    claimed_words.remove(guessed_word)

        return False

    return backtrack(0, 0)

if __name__ == "__main__":
    possible = wordPattern("abba", "dog dog cat dog")
    print(possible)