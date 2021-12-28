import functools


class Alphabet:
    def __init__(self, value: str, freq: float):
        self.value: str = value
        self.freq: float = freq


def cmp(x: Alphabet, y:Alphabet) -> int:
    if x.freq == y.freq:
        if x.value.upper() == y.value.upper():
            if (x.value.isupper() and y.value.isupper()) or (x.value.islower() and y.value.islower()):
                return 0
            return 1 if x.value.isupper() else -1
        return 1 if x.value.upper() > y.value.upper() else -1
    return 1 if x.freq < y.freq else -1


t = int(input())
for i in range(t):
    freq_seq = map(float, input().split())
    freq_list = [j for j in freq_seq]
    sentence = input()
    alphabet_list = []
    for c in sentence:
        if c >= 'a':
            alphabet_list.append(Alphabet(c, freq_list[ord(c)-ord('a')]))
        else:
            alphabet_list.append(Alphabet(c, freq_list[ord(c)-ord('A')]))
    alphabet_list.sort(key=functools.cmp_to_key(cmp))
    print("case #{:d}:".format(i))
    for alphabet in alphabet_list:
        print(alphabet.value, end='')
    print()
