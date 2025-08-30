import sys; input = sys.stdin.readline

n, m = map(int, input().split())
s = [input().rstrip() for _ in range(n)]
prefixes = [input().rstrip() for _ in range(m)]
s.sort()
prefixes.sort()

cnt = 0
i, j = 0, 0
while i < n and j < m:
    if s[i][:len(prefixes[j])] == prefixes[j]:
        cnt += 1
        j += 1
    elif s[i] > prefixes[j]:
        j += 1
    else:
        i += 1
print(cnt)