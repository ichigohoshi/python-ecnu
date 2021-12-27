n = int(input())
string_list = []
for i in range(n):
    string_list.append(input())
for i in reversed(sorted(string_list)):
    print(i)
