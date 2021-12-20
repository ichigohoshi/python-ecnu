from math import pow

while True:
    try:
        a, b = map(int, input().split())
        print("{:.3f}".format(pow(a, b)))
    except:
        break
