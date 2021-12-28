import functools


class Student:
    def __init__(self, sid, grade):
        self.sid = sid
        self.grade = grade


def cmp(x: Student, y: Student) -> int:
    if x.grade == y.grade:
        return x.sid - y.sid
    return y.grade - x.grade


n = int(input())
students = []
for i in range(n):
    sid, grade = map(int, input().split())
    if grade >= 60:
        students.append(Student(sid, grade))
students.sort(key=functools.cmp_to_key(cmp))
for student in students:
    print("{:d} {:d}".format(student.sid, student.grade))
