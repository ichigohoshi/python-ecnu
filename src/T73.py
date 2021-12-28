import functools


class Linkman:
    def __init__(self, title: str, phone: str):
        self.title: str = title
        self.phone: str = phone


def cmp(x: Linkman, y: Linkman) -> int:
    if x.title == y.title:
        if x.phone == y.phone:
            return 0
        return 1 if x.phone > y.phone else -1
    return 1 if x.title > y.title else -1


t = int(input())
for i in range(t):
    n = int(input())
    linkman_list = []
    for j in range(n):
        temp_title, temp_phone = map(str, input().split())
        linkman_list.append(Linkman(temp_title, temp_phone))
    sub_phone = input()
    linkman_list.sort(key=functools.cmp_to_key(cmp))
    print("case #{:d}:".format(i))
    count = 0
    result = ""
    for linkman in linkman_list:
        if linkman.phone.__contains__(sub_phone):
            result += "{} {}\n".format(linkman.title, linkman.phone)
            count += 1
    print(count)
    print(result, end='')
