from math import sqrt

prime = []
for i in range(2, 50000):
    flag = True
    for j in range(2, int(sqrt(i))+1):
        if i % j == 0:
            flag = False
            break
    if flag:
        prime.append(i)

t = int(input())
for i in range(t):
    n = int(input())
    k = 1
    for k in prime:
        if n % k == 0:
            break
    print("case #{:d}:\n{:d}".format(i, n//k))
