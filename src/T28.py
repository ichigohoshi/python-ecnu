n = int(input())
for i in range(n):
    all_money, single_zongzi_money = map(int, input().split())
    three_zongzi_money = 3 * single_zongzi_money
    five_zongzi_money = 5 * single_zongzi_money
    max_single_num = all_money//single_zongzi_money
    max_three_num = all_money//three_zongzi_money
    result = 0
    for three_num in range(0, max_three_num+1):
        five_num = (max_single_num - three_num * 3) // 5
        result = max(result, max_single_num + five_num * 2 + three_num)
    print(result)
