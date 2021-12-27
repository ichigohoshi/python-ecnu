factorial = []
result = []
pointer = 0
factorial.append(1)
result.append(0)
for i in range(1, 1001):
    factorial.append(i * factorial[pointer])
    pointer += 1
    i_str = str(factorial[pointer])
    count = 0
    for i_char in reversed(i_str):
        if i_char != '0':
            break
        count += 1
    result.append(count)
n = int(input())
for i in range(n):
    num = int(input())
    print("case #{:d}:\n{:d}".format(i, result[num]))
