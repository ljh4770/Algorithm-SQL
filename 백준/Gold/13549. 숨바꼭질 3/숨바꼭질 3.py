from collections import deque
import heapq

def dijkstra(length, n, k):
    push = heapq.heappush
    pop = heapq.heappop

    heap = []
    push(heap, (0, n))
    times = [float('inf')] * length
    times[n] = 0

    dxdt = [(lambda x: x - 1, 1), (lambda x: x + 1, 1), (lambda x: x * 2, 0)]

    while heap:
        time, x = pop(heap)
        if x == k:
            return time

        if times[x] < time:
            continue

        for dx, dt in dxdt:
            nx = dx(x)
            nt = time + dt

            if not (0 <= nx < length):
                continue

            if nt < times[nx]:
                times[nx] = nt
                push(heap, (nt, nx))
    
    return times

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    n, k = map(int, input().split(' '))
    
    time = dijkstra(100001, n, k)
    print(time)