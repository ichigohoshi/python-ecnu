n = int(input())
alpha_list = []
for i in range(n):
    sentence = input()
    for c in sentence:
        if c.isalpha():
            alpha_list.append(c)
    alpha_list = sorted(alpha_list, reverse=True)
    new_sentence = ""
    for c in sentence:
        if c.isalpha():
            new_sentence += alpha_list.pop()
        else:
            new_sentence += c
    print("case #{:d}:\n{}".format(i, new_sentence))
