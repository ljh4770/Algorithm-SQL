import sys
num = sys.stdin.readline().rstrip()

counts = [0] * 10

for n in num:
    counts[int(n)] += 1

for n in range(9, -1, -1):
    for _ in range(counts[n]):
        print(n, end='')
print()