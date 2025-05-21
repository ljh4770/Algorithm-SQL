from collections import Counter

A = int(input())
B = int(input())
C = int(input())

res = str(A * B * C)
cnt = Counter(res)

for i in range(0, 10):
    print(cnt[str(i)])
