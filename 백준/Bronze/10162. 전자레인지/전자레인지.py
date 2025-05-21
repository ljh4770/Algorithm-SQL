import sys

time = int(sys.stdin.readline())
btns = [5 * 60, 60, 10]

answer = [0, 0, 0]
for i in range(3):
    if time % btns[i] >= 0:
        answer[i] = time // btns[i]
        time = time % btns[i]
if time != 0:
    print(-1)
else:
    for i in range(3):
        print(answer[i], end=' ')
    print()