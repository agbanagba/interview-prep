def to_goat_latin(s):
    vowel = ['a', 'e', 'i', 'o', 'u']
    gl = ""
    for idx, word in enumerate(s.split(' ')):
        if word[0].lower() in vowel:
            word += 'ma'
        else:
            word = word[1:len(word)] + word[0] + 'ma'
        gl += word + 'a' * (idx + 1) + ' '
    return gl.rstrip(' ')


if __name__ == '__main__':
    ss = "I speak Goat Latin"
    ss2 = "The quick brown fox jumped over the lazy dog"
    print(to_goat_latin(ss2))
