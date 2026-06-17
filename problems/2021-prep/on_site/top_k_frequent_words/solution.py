import heapq


class Word(object):
    def __init__(self, count, word):
        self.word = word
        self.count = count

    def __gt__(self, other):
        if self.count > other.count:
            return True
        elif self.count < other.count:
            return False

        # Simply compare both self.word and other.word
        return self.word > other.word


def top_k_frequent(words, k):
    frequency_map = {}

    for word in words:
        frequency_map[word] = frequency_map.get(word, 0) + 1

    vals = sorted(frequency_map.items(), key=lambda x: (x[1], x[0]))
    # return [key for key, value in vals]
    return vals


def top_k_frequent_heap(words, k):
    frequency_map = {}

    for word in words:
        frequency_map[word] = frequency_map.get(word, 0) + 1

    # Put it in a heapq and pop until values in it is k most
    heap = [(-value, key) for key, value in frequency_map.items()]
    heapq.heapify(heap)
    return [heapq.heappop(heap)[1] for _ in range(k)]
    # for key, value in frequency_map.items():
    #     heapq.heappush(heap, Word(value, key))
    #     if len(heap) > k:
    #         heapq.heappop(heap)
    #
    # return [(word.word, word.count) for word in sorted(heap, reverse=True)]


if __name__ == '__main__':
    wrds = ['i', 'love', 'leetcode', 'i', 'love', 'coding']
    wrds2 = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
    print(top_k_frequent_heap(wrds, 2))
    print(top_k_frequent_heap(wrds2, 4))
