while True:
    try:
        n = int(input())
        # 已经证实存在n==0然后直接无换行接下一个case的情况
        if n == 0:
            print("None None")
        nums = map(int, input().split())
        odd_count = 0
        odd_sum = 0.0
        even_count = 0
        even_sum = 0.0
        for i in nums:
            if i % 2 == 0:
                even_count += 1
                even_sum += i
            else:
                odd_count += 1
                odd_sum += i
        # 应该输出三位小数，虽然题目说的是三位有效数字
        odd_result = "None" if odd_count == 0 else "{:.3f}".format(odd_sum / odd_count)
        even_result = "None" if even_count == 0 else "{:.3f}".format(even_sum / even_count)
        print("{} {}".format(odd_result, even_result))
    except:
        break
