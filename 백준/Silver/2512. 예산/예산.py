import sys
input = sys.stdin.readline

n = int(input())
req = [*map(int, input().split(' '))]
m = int(input())

# Sum of requests is less than the budget(m)
if sum(req) < m:
    print(max(req))
    sys.exit(0)

result = 0 # Answer: upper bound of the request
start, end = 1, max(req)
while start <= end:
    mid = (start + end) // 2 # Temporary upper bound
    tot = 0

    for r in req:
        if r > mid: # Greater than the upper bound
            tot += mid
        else: # LEQ than the upper bound
            tot += r
    
    if tot <= m:
        # Temporary upper bound is valid
        # May need to increase the upper bound
        result = mid # Update the upper bound
        start = mid + 1
    else:
        # Temporary upper bound is too high
        # Decrease the temporary upper bound
        end = mid - 1

print(result)