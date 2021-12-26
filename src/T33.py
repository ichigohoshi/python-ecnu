from math import gcd

n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    a_b_gcd = gcd(a, b)
    a_b_lcm = a * b // a_b_gcd
    print("{:d} {:d}".format(a_b_gcd, a_b_lcm))
