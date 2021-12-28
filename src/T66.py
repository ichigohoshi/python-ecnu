n = int(input())
for i in range(n):
    sentence = input()
    new_sentence = ""
    for c in sentence:
        new_sentence += chr((ord(c) + 1 - ord('A')) % 26 + ord('A'))
    print("case #{:d}:\n{}".format(i, new_sentence))
