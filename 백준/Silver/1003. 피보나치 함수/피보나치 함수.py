import sys

input = sys.stdin.readline

T = int(input())
data = [int(input()) for _ in range(T)]

fibo = [(0, 0)] * 41
fibo[0] = (1, 0)
fibo[1] = (0, 1)

for i in range(2, 41, 1):
    zero = fibo[i - 1][0] + fibo[i - 2][0]
    one = fibo[i - 1][1] + fibo[i - 2][1]
    fibo[i] = (zero, one)

for num in data:
    print(fibo[num][0], fibo[num][1])
