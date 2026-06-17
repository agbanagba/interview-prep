import collections
from collections import defaultdict


def ladder_length(begin_word, end_word, word_list):
    if end_word not in word_list or not end_word or not begin_word or not word_list:
        return 0

    buckets = defaultdict(list)
    for word in word_list:
        for i in range(len(begin_word)):
            bucket = word[:i] + '_' + word[i + 1:]
            buckets[bucket].append(word)

    queue = collections.deque()
    queue.append((begin_word, 1))
    visited = {begin_word: True}

    while queue:
        curr_word, level = queue.popleft()
        for i in range(len(begin_word)):
            wd = curr_word[:i] + '_' + curr_word[i + 1:]
            for word in buckets[wd]:
                if word == end_word:
                    return level + 1

                if word not in visited:
                    visited[word] = True
                    queue.append((word, level + 1))

    return 0


if __name__ == '__main__':
    begin, end, wrd_list = "hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]
    print(ladder_length(begin, end, wrd_list))
