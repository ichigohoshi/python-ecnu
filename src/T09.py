from math import sqrt

g = 9.8
while True:
    n = int(input())
    if n == 0:
        break
    h = 1.75
    for i in range(1, 3):
        if i == n:
            break
        h += 5
    for i in range(3, n):
        h += 3
    print("{:.3f}".format(round(sqrt(2*h/g), 3)))
