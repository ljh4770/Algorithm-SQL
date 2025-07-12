from math import gcd

a_son, a_mom = map(int, input().split())
b_son, b_mom = map(int, input().split())

son = a_son * b_mom + a_mom * b_son
mom = a_mom * b_mom

g = gcd(son, mom)
son //= g
mom //= g

print(son, mom)