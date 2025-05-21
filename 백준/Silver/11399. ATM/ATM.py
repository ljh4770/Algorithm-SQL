import sys
input = sys.stdin.readline

n = int(input())
times = list(map(int, input().split(' ')))
times.sort()
cum_sum = [0] * n
cum_sum[0] = times[0]

for i in range(1, n, 1):
    cum_sum[i] = cum_sum[i - 1] + times[i]

print(sum(cum_sum))