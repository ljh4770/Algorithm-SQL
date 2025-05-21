import sys
input = sys.stdin.readline

n = int(input())
values = [*map(int, input().split(' '))]

sum_ = float('inf')
l = 0
r = n - 1

basic = 0
acid = 0

while l < r:
    sum_tmp = values[l] + values[r]
    if abs(sum_tmp) < sum_:
        basic = values[l]
        acid = values[r]
        sum_ = abs(sum_tmp)

        if sum_ == 0:
            break
    if sum_tmp < 0:
        l += 1
    
    else:
        r -= 1

print(basic, acid)