import sys
input = sys.stdin.readline

n = int(input())
data = [tuple(map(int, input().split(' '))) for _ in range(n)]

for i in range(n):
    cnt = 1
    for j in range(n):
        if data[j][0] > data[i][0] and data[j][1] > data[i][1]:
            cnt += 1
        else:
            continue
    print(cnt)