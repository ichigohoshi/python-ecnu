from math import sqrt

prime = []
for i in range(2, 20001):
    flag = True
    for j in range(2, int(sqrt(i))+1):
        if i % j == 0:
            flag = False
            break
    if flag:
        prime.append(i)
t = int(input())
result = ""
for i in range(t):
    num = int(input())
    for j in prime:
        if num == 1:
            break
        count = 0
        while num % j == 0:
            count += 1
            num //= j
        if count > 0:
            result += "({:d},{:d})".format(j, count)
    result += '\n'
print(result, end='')
