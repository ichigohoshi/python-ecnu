def f(n, x):
    a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
         'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    b = []
    flag = False
    if n < 0:
        n = -n
        flag = True
    while True:
        s = n // x
        y = n % x
        b = b + [y]
        if s == 0:
            break
        n = s
    b.reverse()
    if flag:
        print('-', end='')
    for i in b:
        print(a[i], end='')
    print()


n = int(input())
for i in range(n):
    n, r = map(int, input().split())
    f(n, r)
