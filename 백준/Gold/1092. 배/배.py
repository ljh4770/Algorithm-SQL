import sys; input = sys.stdin.readline

n = int(input())
limits = [*map(int, input().split())]
m = int(input())
weights = [*map(int, input().split())]

limits.sort(reverse=True)
weights.sort(reverse=True)

if limits[0] < weights[0]:
    print(-1)
    sys.exit()

cnt = 0
while weights:
    for lim in limits:
        if weights and lim < weights[-1]:
            continue
        
        for i, w in enumerate(weights):
            if lim >= w:
                del weights[i]
                break
    cnt += 1

print(cnt)