import sys
input = sys.stdin.readline

n = int(input())
meetings = [tuple(map(int, input().split(' '))) for _ in range(n)]
meetings.sort(key=lambda x: (x[1], x[0]))

cnt = 1
last_end = meetings[0][1]

for meet in meetings[1:]:
    start, end = meet
    if start >= last_end:
        cnt += 1
        last_end = end

print(cnt)