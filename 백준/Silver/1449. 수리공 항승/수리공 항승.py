import sys; input = sys.stdin.readline

n, l = map(int, input().split())
positions = [*map(int, input().split())]
positions.sort()

cnt = 1
start = positions[0] - 0.5
end = start + l
for pos in positions[1:]:
    if start < pos < end:
        continue
    start = pos - 0.5
    end = start + l
    cnt += 1

print(cnt)