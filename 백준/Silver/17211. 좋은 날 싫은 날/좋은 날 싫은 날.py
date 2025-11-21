import sys; input = sys.stdin.readline


n, today = map(int, input().split())
props = [*map(float, input().split())]
# 0 -> 0 / 0 -> 1 / 1 -> 0 / 1 -> 1

results = [0, 0]
if today == 0:
    results[0] = 1
else:
    results[1] = 1

for _ in range(n):
    prev = results[0]
    results[0] = results[0] * props[0] + results[1] * props[2]
    results[1] = prev * props[1] + results[1] * props[3]

for p in results:
    print(int(p * 1000))