t = int(input())
for i in range(t):
    n = int(input())
    num_count_map = {}
    nums = map(int, input().split())
    for num in nums:
        if num_count_map.get(num):
            num_count_map[num] += 1
        else:
            num_count_map[num] = 1
    max_k = 0
    max_v = 0
    for k, v in num_count_map.items():
        if v > max_v:
            max_k = k
            max_v = v
    print("case #{:d}:\n{:d}".format(i, max_v))
