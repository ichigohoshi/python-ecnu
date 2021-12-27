n = int(input())
for i in range(n):
    num = int(input())
    nums = map(int, input().split())
    num_list = [j for j in nums]
    while True:
        flag = True
        for j in range(num):
            count = 0
            for k in range(j, num):
                if num_list[k] < num_list[j]:
                    count += 1
            if count != num_list[j]:
                num_list[j] = count
                flag = False
        if flag:
            break
    print("case #{:d}:".format(i))
    for j in range(num-1):
        print(num_list[j], end=' ')
    print(num_list[num-1])
