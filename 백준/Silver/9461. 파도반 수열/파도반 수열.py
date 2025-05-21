import sys
input = sys.stdin.readline

T = int(input())
data = [int(input()) for _ in range(T)]

max_num = max(data)

memo = [0] * (max_num + 1)
memo[1] = 1
memo[2] = 1
memo[3] = 1
memo[4] = 2
memo[5] = 2
memo[6] = 3
memo[7] = 4
memo[8] = 5
memo[9] = 7

big_idx = 9
small_idx = 5

for i in range(10, max_num + 1, 1):
    memo[i] = memo[big_idx] + memo[small_idx]
    big_idx += 1
    small_idx += 1

for num in data:
    print(memo[num])