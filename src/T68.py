n = int(input())
for i in range(n):
    sentence = input()
    new_sentence = ""
    for j in range(len(sentence)):
        if j % 2 == 0:
            if sentence[j].isupper():
                new_sentence += sentence[j].lower()
            else:
                new_sentence += sentence[j]
        else:
            new_sentence += sentence[j]
    print("case #{:d}:\n{}".format(i, new_sentence))
