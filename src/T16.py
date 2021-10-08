import sys

count = 0
sum_ans = 0
max_ans = 0
line = ""
temp = 0
for s in sys.stdin:
    line = s
    temp = len(s)-1
    if temp == 0:
        break
    count += 1
    sum_ans += temp
    max_ans = max(max_ans, temp)
print(str(sum_ans) + ',' + str(count) + ',' + str(max_ans))
