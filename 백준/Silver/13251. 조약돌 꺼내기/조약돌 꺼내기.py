from math import comb

m = int(input())
colors = [*map(int, input().split())]
k = int(input())

numerator = 0
for c in colors:
    if c < k:
        continue
    numerator += comb(c, k)

denominator = comb(sum(colors), k)

print(numerator / denominator)