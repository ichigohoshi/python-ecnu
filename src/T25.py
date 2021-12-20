while True:
    try:
        # 计算位数得按二进制算，注意去掉先导0b
        n = str(bin(int(input())))[2:]
        # 补齐0方便操作
        n_prefix = "0" * (32 - len(n))
        n = n_prefix + n
        # 直接换位
        str_a = n[16:32]    # 高16位拿到原本低16位的数据
        str_b = n[0:16]     # 低16位拿到原本高16位的数据
        # 低16位按位取反
        str_b_reverse = ""
        for i in range(16):
            str_b_reverse += "0" if str_b[i] == "1" else "1"
        str_b = str_b_reverse
        # 高16位跟低16位按位异或后存储在高位
        str_a_xor = ""
        for i in range(16):
            str_a_xor += "0" if str_a[i] == str_b[i] else "1"
        str_a = str_a_xor
        # 组合生成的数字
        str_ab = str_a + str_b
        int_ab = hex(int(str_ab, 2))
        str_ab = str(int_ab)[2:]
        str_ab = str_ab.upper()
        # 补充先导0
        str_ab_prefix = "0" * (8 - len(str_ab))
        str_ab = str_ab_prefix + str_ab
        print(str_ab)
    except:
        break
