import functools


class List:
    def __init__(self, nums, index):
        self.index = index
        self.nums = nums
        self.sum_num = sum(nums)
        self.length = len(nums)


def cmp(x: List, y: List) -> int:
    if x.sum_num != y.sum_num:
        return x.sum_num - y.sum_num
    for i in range(x.length):
        if x.nums[i] != y.nums[i]:
            return x.nums[i] - y.nums[i]
    return x.index - y.index


t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    nums_list = []
    nums = []
    temp_nums_list = []
    sorted_lists = []
    for j in range(n):
        num_seq = map(int, input().split())
        nums = [k for k in num_seq]
        nums_list.append(nums)
        temp_nums_list.append([k for k in nums])
    for j in range(n):
        sorted_lists.append(List(temp_nums_list[j], j))
    sorted_lists.sort(key=functools.cmp_to_key(cmp))
    print("case #{:d}:".format(i))
    for j in sorted_lists:
        temp_list = nums_list[j.index]
        for k in range(m-1):
            print(temp_list[k], end=' ')
        print(temp_list[m-1])
