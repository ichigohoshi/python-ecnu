num, p, n = map(int, input().split())
b_num = bin(num)[2:]
length = len(b_num)
for i in range(32-length):
    b_num = '0' + b_num
ans = b_num[0:32-p-1]
for i in range(32-p-1, 32-p+n-1):
    ans += '0' if b_num[i] == '1' else '1'
ans += b_num[32-p+n-1:]
print(int(ans, 2))
