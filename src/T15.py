s = input()
ans = ""
for i in s:
    if i.isupper():
        ans += i.lower()
    elif i.islower():
        ans += i.upper()
    else:
        ans += i
print(ans)
