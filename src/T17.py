a, b = map(int, input().split())
print("{}\n{}".format(0 if a == 0 or b == 0 else 1, a & b))
