n = int(input())
for i in range(n):
    nums = map(int, input().split('.'))
    num_list = [j for j in nums]
    flag = True
    j_flag = -1
    for j in range(4):
        if num_list[j] < 0 or num_list[j] > 255:
            j_flag = j
            flag = False
            break
    print("case #{:d}:".format(i))
    if flag:
        print("Yes")
    else:
        print("{} {:d} {:d}".format("No", j_flag, num_list[j_flag]))
