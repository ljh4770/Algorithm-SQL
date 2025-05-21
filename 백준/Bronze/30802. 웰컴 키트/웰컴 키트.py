import sys
input = sys.stdin.readline

n = int(input())
sizes = list(map(int, input().split(' ')))
t, p = map(int, input().split(' '))

num_t = 0
for size in sizes:
    num_t += size // t
    if size % t > 0:
        num_t += 1

num_p = n // p
num_1 = n % p

print(num_t)
print(num_p, num_1)