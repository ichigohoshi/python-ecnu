while True:
    try:
        n = int(input())
        num_map = {}
        nums = map(int, input().split())
        for num in nums:
            num_map[abs(num)] = num
        result = ""
        count = 0
        for k, v in sorted(num_map.items()):
            count += 1
            result += "{:d} ".format(v) if count < n else "{:d}".format(v)
        print(result)
    except:
        break
