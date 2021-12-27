n = int(input())
for i in range(n):
    name = input()
    ascii_sum_list = [0, 0, 0, 0, 0, 0]
    for j in range(len(name)):
        ascii_sum_list[j % 6] += ord(name[j])
    result = ""
    for j in range(6):
        result += str(ascii_sum_list[j] % 10)
    print("case #{:d}:\n{}".format(i, result))
