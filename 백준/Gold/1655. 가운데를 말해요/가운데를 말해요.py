import sys
import heapq

input = sys.stdin.readline
N = int(input())
data = [int(input()) for _ in range(N)]

left = []
right = []

for num in data:
    if not left or num <= -left[0]:
        heapq.heappush(left, -num)
    else:
        heapq.heappush(right, num)
    
    if len(left) < len(right):
        value = heapq.heappop(right)
        heapq.heappush(left, -value)

    elif len(left) - len(right) > 1:
        value = -heapq.heappop(left)
        heapq.heappush(right, value)
    
    print(-left[0])
