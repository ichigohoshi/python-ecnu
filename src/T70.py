def sort_strings(p, n):
    nums = []
    for i in range(20):
        nums.append(list())
    for p_str in p:
        flag = True
        for p_char in p_str:
            if p_char.isdigit():
                nums[int(p_char)].append(p_str)
                flag = False
                break
        if flag:
            nums[15].append(p_str)
    nums[15].sort()
    count = 0
    for i in nums[15]:
        p[count] = i
        count += 1
    for i in range(10):
        nums[i].sort()
        for j in nums[i]:
            p[count] = j
            count += 1


if __name__ == '__main__':
    cas = int(input())
    for i in range(cas):
        n = int(input())
        p = []
        p_seq = input().split()
        for j in p_seq:
            p.append(j)
        sort_strings(p, n)
        print("case #{:d}:".format(i))
        for j in range(n-1):
            print(p[j], end=' ')
        print(p[n-1])
