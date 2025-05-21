import sys
from collections import deque

class IntQueue():
    def __init__(self):
        self.queue = deque()
        self.len = 0

    def __len__(self):
        return self.len

    def push(self, X):
        self.len += 1
        self.queue.append(X)
        return None

    def pop(self):
        if self.size() == 0:
            return -1
        
        self.len -= 1

        return self.queue.popleft()
        
    def size(self):
        return self.len

    def empty(self):
        if self.size() == 0:
            return 1
        return 0

    def front(self):
        if self.size() == 0:
            return -1
        return self.queue[0]

    def back(self):
        if self.size() == 0:
            return -1
        return self.queue[-1]
    
N = int(sys.stdin.readline().strip())
queries = [sys.stdin.readline().strip() for _ in range(N)]

int_queue = IntQueue()

for q in queries:
    if ' ' in q:
        op, X = q.split(' ')
    else:
        op = q
    
    if op == 'push':
        int_queue.push(X)
    else:
        if op == 'pop':
            res = int_queue.pop()
        elif op == 'size':
            res = int_queue.size()
        elif op == 'empty':
            res = int_queue.empty()
        elif op == 'front':
            res = int_queue.front()
        elif op == 'back':
            res = int_queue.back()
        print(res)