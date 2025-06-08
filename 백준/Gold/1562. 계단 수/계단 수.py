import sys
n = int(input())
if n < 10:
    print(0)
    sys.exit()

MOD = 10 ** 9
DP = [[[0] * (2 ** 10) for _ in range(10)] for _ in range(n + 1)]

# Initialize the base case
for d in range(10):
  DP[1][d][1 << d] = 1

for i in range(1, n, 1):
  for d in range(10):
    for b in range(2 ** 10):
      if 0 <= d < 9:
        more = b | 1<< (d + 1)
        DP[i + 1][d + 1][more] += DP[i][d][b]
        DP[i + 1][d + 1][more] %= MOD
      if 0 < d <= 9:
        less = b | 1 << (d - 1)
        DP[i + 1][d - 1][less] += DP[i][d][b]
        DP[i + 1][d - 1][less] %= MOD

total = 0
for d in range(1, 10):
  total += DP[n][d][0b1111111111]
  total %= MOD
print(total)