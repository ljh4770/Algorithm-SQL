import sys
input = sys.stdin.readline

n = int(input())
values = [*map(int, input().split(' '))]
values.sort()

min_abs = float('inf') # Sum of values s.t. closest to zero
result = [0] * 3 # Answer: values of three numbers
for i in range(0, n - 2, 1): # pivot
    # Two pointers
    start = i + 1
    end = n - 1
    while start < end:
        total = values[i] + values[start] + values[end]
        if abs(total) < min_abs:
            min_abs = abs(total)
            result[0] = values[i]
            result[1] = values[start]
            result[2] = values[end]
        
        if total < 0:
            start += 1
        elif total > 0:
            end -= 1
        else:
            break

print(*result)