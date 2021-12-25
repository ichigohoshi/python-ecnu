import math

n = int(input())
for i in range(n):
    s, k = map(int, input().split())
    # 不写成 1.0 容易导致 OverflowError: int too large to convert to float
    base = 1.0
    s **= 2
    result = 0
    for j in range(k):
        # 直接 * s 容易导致 OverflowError: int too large to convert to float
        result += (1 - math.pi / 4) / base
        base *= 2
    result *= s
    print("case #{:d}:\n{:.6f}".format(i, result))
