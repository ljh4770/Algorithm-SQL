import sys; input = sys.stdin.readline

n = int(input())
logs = [input().strip() for _ in range(n)]

result = 0
tmp = []
for i in range(n):
    if logs[i] == 'ENTER':
        result += len(set(tmp))
        tmp = []
    else:
        tmp.append(logs[i])
result += len(set(tmp))

print(result)