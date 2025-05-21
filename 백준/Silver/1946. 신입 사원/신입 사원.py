import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    scores = [tuple(map(int, input().split(' '))) for _ in range(n)]

    scores.sort(key=lambda x: x[0])
    
    cnt = 1
    max_ = scores[0][1]
    for i in range(n):
        if max_ > scores[i][1]:
            cnt += 1
            max_ = scores[i][1]
    print(cnt)