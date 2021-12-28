import functools


class Point:
    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y
        self.quadrant: int
        if x >= 0 and y >= 0:
            self.quadrant = 1
        elif y >= 0:
            self.quadrant = 2
        elif x >= 0:
            self.quadrant = 4
        else:
            self.quadrant = 3


def cmp(x: Point, y: Point) -> int :
    if x.x * x.x + x.y * x.y == y.x * y.x + y.y * y.y:
        if x.quadrant == y.quadrant:
            if abs(x.x) == abs(y.x):
                return 0
            return 1 if abs(x.x) > abs(y.x) else -1
        return 1 if x.quadrant > y.quadrant else -1
    return 1 if x.x * x.x + x.y * x.y > y.x * y.x + y.y * y.y else -1


cas = int(input())
for i in range(cas):
    n = int(input())
    point_list = []
    for j in range(n):
        temp_x, temp_y = map(int, input().split())
        point_list.append(Point(temp_x, temp_y))
    point_list.sort(key=functools.cmp_to_key(cmp))
    print("case #{:d}:".format(i))
    for j in range(n-1):
        print("({:d},{:d})".format(point_list[j].x, point_list[j].y), end=' ')
    print("({:d},{:d})".format(point_list[n-1].x, point_list[n-1].y))
