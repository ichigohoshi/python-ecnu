n = eval(input())
for i in range(n):
    s = input()
    a = int(s[0:8], 2)
    b = int(s[8:16], 2)
    c = int(s[16:24], 2)
    d = int(s[24:32], 2)
    print("{}.{}.{}.{}".format(a, b, c, d))
