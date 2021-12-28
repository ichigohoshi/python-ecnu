sentence = input().replace(' ', '')
count_list = [0] * 26
for ch in sentence:
    count_list[ord(ch)-ord('a')] += 1
max_count = 0
max_index = 0
for i in range(26):
    if count_list[i] > max_count:
        max_index = i
        max_count = count_list[i]
print("{} {:.2f}".format(chr(max_index+ord('a')), max_count/len(sentence)))
