n = int(input())
for i in range(n):
    num = int(input())
    num_bin_str = str(bin(num))[2:]
    length = len(num_bin_str)
    if length > 334:
        num_bin_str = num_bin_str[length-334: length]
    new_num_bin_str = ""
    for num_bit in reversed(num_bin_str):
        new_num_bin_str += num_bit
    new_num = int(new_num_bin_str, 2)
    print("case #{:d}:\n{:d}".format(i, new_num))
