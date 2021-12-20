from math import sqrt

while True:
    try:
        a, b = map(int, input().split())
        print("{:.3f}".format(sqrt(a*a+b*b)))
    except:
        break
