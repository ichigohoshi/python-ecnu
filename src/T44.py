n = int(input())
n_bin_str = str(bin(n))
count = 0
for i in n_bin_str:
    if i == "1":
        count += 1
print(count)
