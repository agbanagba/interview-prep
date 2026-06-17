import collections

# https://leetcode.com/problems/word-ladder-ii/
def find_ladders(begin_word, end_word, word_list):
    if end_word not in word_list or not end_word or not begin_word or not word_list:
        return []

    buckets = collections.defaultdict(list)
    for word in word_list:
        for i in range(len(begin_word)):
            bucket = word[:i] + '_' + word[i + 1:]
            buckets[bucket].append(word)

    queue = collections.deque()
    queue.append((begin_word, 1))
    visited = {begin_word: True}
    transformations = []

    transformation = [begin_word]

    while queue:
        curr_word, level = queue.popleft()
        for i in range(len(begin_word)):
            wd = curr_word[:i] + '_' + curr_word[i + 1:]
            for word in buckets[wd]:
                if word not in visited:
                    if word == end_word:
                        transformations.append(transformation)
                    else:
                        transformation.append(word)

                    visited[word] = True
                    queue.append((word, level + 1))

    return transformations


if __name__ == '__main__':
    begin, end, wrd_list = "hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]
    print(find_ladders(begin, end, wrd_list))
