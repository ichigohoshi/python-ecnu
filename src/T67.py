n, m = map(int, input().split())
nums = map(int, input().split())
num_list = [i for i in nums]
num_list = num_list[n-m:] + num_list[:n-m]
for i in range(n-1):
    print(num_list[i], end=' ')
print(num_list[n-1])
