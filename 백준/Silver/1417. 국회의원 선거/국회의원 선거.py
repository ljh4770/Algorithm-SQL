import sys; input = sys.stdin.readline


n = int(input())
scores = [int(input()) for _ in range(n)]

if n ==1:
    print(0)
    sys.exit()

cnt = 0
base = scores[0]
targets = sorted(scores[1:], reverse=True)

while targets[0] >= base:
    base += 1
    targets[0] -= 1
    cnt += 1
    targets.sort(reverse=True)

print(cnt)
