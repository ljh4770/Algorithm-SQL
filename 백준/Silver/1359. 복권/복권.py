from math import comb

n, m, k = map(int, input().split())

result = 0

while k <= m:
    intersection = comb(n, k)
    left = comb(n - k, m - k)
    right = comb(n - m, m - k)

    denominator = comb(n, m)

    result += intersection * left * right / (denominator ** 2)
    k += 1

print(result)