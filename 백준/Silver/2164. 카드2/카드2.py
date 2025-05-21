import sys
import queue

N = int(sys.stdin.readline())

q = queue.Queue()

for n in range(1, N + 1, 1):
    q.put(n)

while q.qsize() != 1:
    q.get()
    item = q.get()
    q.put(item)

print(q.get())
