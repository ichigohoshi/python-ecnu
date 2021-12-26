tribonacci = {
    0: 0,
    1: 1,
    2: 1
}
a = 0
b = 1
c = 1
for i in range(3, 40):
    tribonacci[i] = a + b + c
    a = b
    b = c
    c = tribonacci[i]
n = int(input())
for i in range(n):
    num = int(input())
    print("case #{:d}:\n{:d}".format(i, tribonacci[num]))
