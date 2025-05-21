import sys
input = sys.stdin.readline

n, m = map(int, input().split(' '))
known = list(map(int, input().split(' ')))
party = [list(map(int, input().split(' '))) for _ in range(m)]
is_known = [False] * (n + 1)

if len(known) == 1:
    print(m)
    sys.exit(0)

for k in known[1:]:
    is_known[k] = True

for _ in range(m):
    for p in party:
        for a in p[1:]:
            if is_known[a] == True:
                for a in p[1:]:
                    is_known[a] = True
                break

cnt = 0
for p in party:
    for a in p[1:]:
        if is_known[a] == True:
            break
    else:
        cnt += 1
print(cnt)