from math import sqrt
from math import pow

n = int(input())
grade_sum = 0
grade_list = []
for i in range(n):
    s_id, grade = map(int, input().split())
    grade_sum += grade
    grade_list.append(grade)
grade_avg = grade_sum / n
grade_diff_sum = 0
for i in grade_list:
    grade_diff_sum += pow(grade_avg-i, 2)
# 样本标准差
grade_std = sqrt(grade_diff_sum/(n-1))
print("{:.2f} {:.2f}".format(grade_avg, grade_std))
