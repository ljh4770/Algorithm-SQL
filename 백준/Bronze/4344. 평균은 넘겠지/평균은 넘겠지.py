import sys

C = int(sys.stdin.readline())

for i in range(C):
    q = list(map(int, sys.stdin.readline().split()))
    res = sum(q[1:]) / q[0]

    cnt = 0
    for score in q[1:]:
        if score > res:
            cnt += 1
    print(f"{cnt / q[0]: .3%}")
