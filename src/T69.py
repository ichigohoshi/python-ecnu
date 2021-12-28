import functools


class Word:
    def __init__(self, word):
        self.word = word
        char_set = set()
        for c in word:
            char_set.add(c)
        self.num = len(char_set)


def cmp(x: Word, y: Word) -> int:
    if x.num == y.num:
        return 1 if x.word > y.word else -1
    return y.num - x.num


t = int(input())
for i in range(t):
    n = int(input())
    word_list = []
    for j in range(n):
        word_list.append(Word(input()))
    word_list.sort(key=functools.cmp_to_key(cmp))
    print("case #{:d}:".format(i))
    for j in word_list:
        print(j.word)
