n = int(input())

memo = [0] * (n + 1)
if n == 0:
    print(0)
    exit(0)
memo[1] = 1

for i in range(2, n + 1, 1):
    memo[i] = memo[i - 1] + memo[i - 2]

print(memo[n])