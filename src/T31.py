n = int(input())
for i in range(n):
    num = int(input())
    sum_num = num
    sweet = num % 3
    wrapper = num
    while wrapper >= 3:
        new_num = wrapper // 3
        sum_num += new_num
        sweet += new_num
        wrapper %= 3
        wrapper += new_num
        sweet %= 3
    print(sum_num)
