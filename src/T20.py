from math import gcd
n = int(input())
cnt1 = 0
total = 32
b = bin(n)
for i in range(2, len(b)):
    if b[i] == "1":
        cnt1 += 1
g = 0 if cnt1 == 0 else gcd(total, cnt1)
print("{},{}:{}".format(cnt1, cnt1//g if cnt1 != 0 and g != 0 else cnt1, total//g if total != 0 and g != 0 else total))
