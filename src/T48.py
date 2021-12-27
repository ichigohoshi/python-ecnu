cmd = input()
num_set = set()
# 有可能是换行符分隔
while True:
    try:
        nums = map(int, input().split())
        for i in nums:
            num_set.add(i)
    except:
        break
result = ""
if cmd == 'A':
    for i in sorted(num_set):
        result += "{:d} ".format(i)
else:
    for i in reversed(sorted(num_set)):
        result += "{:d} ".format(i)
result = result[: len(result) - 1]
print(result)
