a, b = map(int, input().split())
print("{}\n{}\n{}".format(0 if a == 0 and b == 0 else 1, a | b, a ^ b))
