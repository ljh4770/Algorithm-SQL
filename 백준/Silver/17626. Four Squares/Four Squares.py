import sys
import math

n = int(sys.stdin.readline())

# 1. n이 완전제곱수인지 확인
if int(math.isqrt(n))**2 == n:
    print(1)
    sys.exit(0)

# 2. n이 두 제곱수 합인지 확인
for i in range(1, int(math.isqrt(n)) + 1):
    remainder = n - i*i
    if int(math.isqrt(remainder))**2 == remainder:
        print(2)
        sys.exit(0)

# 3. 세 제곱수 합인지(혹은 네 제곱수 합인지) 확인
#    => n에서 4로 나누어떨어지는 만큼 나눈 뒤 8로 나눈 나머지가 7이면 네 제곱수 합, 그렇지 않으면 세 제곱수 합
m = n
while m % 4 == 0:
    m //= 4

if m % 8 != 7:
    print(3)
else:
    print(4)
