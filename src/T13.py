from math import *

d, p, r = map(float, input().split())
r *= 0.01
print(round(log10(p/(p-d*r))/log10(1+r)))
