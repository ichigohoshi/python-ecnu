import functools


class List:
    def __init__(self, nums, index):
        self.index = index
        self.nums = nums
        self.length = len(nums)


def cmp(x: List, y: List) -> int:
    for i in range(x.length):
        if x.nums[i] != y.nums[i]:
            return y.nums[i] - x.nums[i]
    return x.index - y.index


t = int(input())
for i in range(t):
    n = int(input())
    nums_list = []
    nums = []
    temp_nums_list = []
    sorted_lists = []
    max_len = 0
    for j in range(n):
        num_seq = map(int, input().split())
        nums = [k for k in num_seq]
        temp_len = len(nums)
        nums.pop()
        nums_list.append(nums)
        temp_nums_list.append([k for k in nums])
        if temp_len > max_len:
            max_len = len(nums)
    for j in range(n):
        j_len = len(temp_nums_list[j])
        for k in range(j_len, max_len):
            temp_nums_list[j].append(-1)
        sorted_lists.append(List(temp_nums_list[j], j))
    sorted_lists.sort(key=functools.cmp_to_key(cmp))
    for j in sorted_lists:
        temp_list = nums_list[j.index]
        temp_len = len(temp_list)
        for k in range(temp_len-1):
            print(temp_list[k], end=' ')
        print(temp_list[temp_len-1])
