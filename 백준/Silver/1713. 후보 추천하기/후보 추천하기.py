import sys
input = sys.stdin.readline
n = int(input())
candidate = int(input())
rec = [*map(int, input().split())]

result = []
cnt = []

for i in rec:
    if i in result:
        cnt[result.index(i)] += 1
    else:
        if len(result) >= n:
            idx = cnt.index(min(cnt))
            del result[idx]
            del cnt[idx]
        result.append(i)
        cnt.append(1)

result.sort()
print(*result)