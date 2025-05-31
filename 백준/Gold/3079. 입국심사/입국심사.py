import sys
input = sys.stdin.readline

# n: number of table
# m: number of people
n, m = map(int, input().split(' '))
times = [int(input()) for _ in range(n)] # time for each table

result = 0 # Answer: Minimal time to serve m people
start, end = min(times), max(times) * m
while start <= end:
    # Temporary time to serve m people
    mid = (start + end) // 2
    cnt = 0 # Served people count

    for time in times:
        # Count how many people can be served in mid time
        cnt += mid // time

    if cnt >= m:
        end = mid - 1
        result = mid
    else:
        start = mid + 1

print(result)