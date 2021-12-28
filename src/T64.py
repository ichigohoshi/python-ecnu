sentence = input().split()
longest_word = ""
longest_length = 0
for word in sentence:
    if len(word) > longest_length:
        longest_length = len(word)
        longest_word = word
print(longest_word)
