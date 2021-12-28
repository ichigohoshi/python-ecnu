n = int(input())
result_list = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 1,
    6: 1,
    7: 1,
    8: 1,
    9: 1,
    10: 2,
    11: 2,
    12: 2,
    13: 2,
    14: 2,
    15: 3,
    16: 3,
    17: 3,
    18: 3,
    19: 3,
    20: 4
}
for i in range(n):
    num = int(input())
    print("case #{:d}:\n{:d}".format(i, result_list[num]))
