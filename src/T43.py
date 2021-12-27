from math import sqrt

n = int(input())
for i in range(n):
    num = int(input())
    m = 2 * int(sqrt(num))
    count = 0
    for j in range(m, 1, -1):
        if (2 * num + j - j * j) % (2 * j) == 0 and (2 * num + j - j * j) > 0:
            count += 1
    print("case #{:d}:\n{:d}".format(i, count))
