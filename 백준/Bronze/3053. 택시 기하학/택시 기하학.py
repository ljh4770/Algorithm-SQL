import sys
from math import pi
input = sys.stdin.readline

r = int(input())
eu = r ** 2 * pi
non_eu = 2 * r ** 2
print(f"{eu:.6f}")
print(f"{non_eu:.6f}")