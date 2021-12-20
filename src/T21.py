import sys

count = 0
for s in sys.stdin:
    line = s
    str_s = line.split()
    for i in str_s:
        if i[0].isupper():
            count += 1
print(count)
