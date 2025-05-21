import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split(' ')))
B = list(map(int, input().split(' ')))
A.sort()
B.sort(key=lambda x: -x)
sum_ = 0
for a, b in zip(A, B):
    sum_ += a * b
print(sum_)