import sys; input = sys.stdin.readline

n, m = map(int, input().split())
arr = [*map(int, input().split())]
 
r = [0] * m
prefix_sum = 0
for i in range(n):
    prefix_sum += arr[i]
    r[prefix_sum % m] += 1

answer = r[0]
for i in range(m):
    answer += r[i] * (r[i] - 1) // 2

print(answer)