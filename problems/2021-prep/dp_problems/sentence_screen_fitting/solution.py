def words_typing_naive(sentence, rows, cols):
    # This solution is funny tbh and works to some extent
    len_sentence = len(sentence) - 1

    for s in sentence:
        len_sentence += len(s)

    return (rows * cols) // len_sentence


def words_typing(sentence, rows, cols):
    pass


if __name__ == '__main__':
    sts = ['hello', 'world']
    print(words_typing_naive(sts, 2, 8))
    print(words_typing_naive(['a', 'bcd', 'e'], 3, 6))
