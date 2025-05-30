import sys
input = sys.stdin.readline

# number of lessons (n) and number of BDs (m)
n, m = map(int, input().split(' '))
# time for each lesson
times = [*map(int, input().split(' '))]

result = 0 # Minimal size per BD
start, end = max(times), sum(times)
while start <= end:
    # Temporary size per BD
    mid = (start + end) // 2
    
    cnt = 1 # Number of segments(BD)
    total = 0 # Saved time per segment(BD)
    for time in times:
        if total + time > mid: # If exceed the size
            cnt += 1 # Increase the number of segments(BD)
            total = time # Reset the saved time for the new segment
        else:
            # Increase the saved time for the current segment
            total += time

    if cnt > m: # If the number of segments exceeds m
        start = mid + 1 # Increase the size per BD
    elif cnt <= m: # If the number of segments is within m
        # Valid
        result = mid # Update the result
        end = mid - 1 # Decrease the size per BD

print(result)