t = int(input())
for i in range(t):
    pow_sum = 0
    n = int(input())
    for j in range(2, n):
        if n % j == 0:
            pow_sum += j * j
    print("case #{:d}:\n{:d}".format(i, pow_sum))
