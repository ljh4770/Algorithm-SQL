import sys
n = int(sys.stdin.readline())

if n == 1:
    print(1)
    sys.exit(0)
elif n == 2:
    print(2)
    sys.exit(0)

memo = [0] * (n + 1)
memo[1] = 1
memo[2] = 2

div = 15746

for i in range(3, n + 1, 1):
    memo[i] = memo[i - 1] + memo[i - 2]
    memo[i] %= div

print(memo[n])