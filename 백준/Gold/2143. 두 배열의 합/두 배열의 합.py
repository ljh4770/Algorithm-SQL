import sys
from collections import Counter
input = sys.stdin.readline

t = int(input())
n = int(input())
a = [*map(int, input().split())]
m = int(input())
b = [*map(int, input().split())]

result = 0
counter = Counter()


for i in range(n):
    for j in range(i, n):
        counter[sum(a[i: j + 1])] += 1

for i in range(m):
    for j in range(i, m):
        sub = t - sum(b[i: j + 1])
        result += counter[sub]
print(result)