import sys
input = sys.stdin.readline

n = int(input())

cnt = dict()
for _ in range(n):
    num = int(input())
    if num in cnt.keys():
        cnt[num] += 1
    else:
        cnt[num] = 1

for i in range(1, max(cnt.keys()) + 1, 1):
    if i not in cnt.keys():
        continue
    for _ in range(cnt[i]):
        print(i)