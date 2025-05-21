import sys

class IntStack:
    def __init__(self):
        self.stack = []

    def push(self, X):
        self.stack.append(X)
        return None

    def pop(self):
        if self.size() != 0:
            return self.stack.pop()
        
        return -1

    def size(self):
        return len(self.stack)

    def empty(self):
        if self.size() == 0:
            return 1
        return 0

    def top(self):
        if self.size() != 0:
            return self.stack[-1]
        return -1
    
my_stack = IntStack()

N = int(sys.stdin.readline())

for i in range(N):
    query = sys.stdin.readline().strip().split(' ')

    if len(query) > 1:
        op = query[0]
        X = int(query[1])
    else:
        op = query[0]
    
    if op == 'push':
        my_stack.push(X)
    elif op == 'pop':
        print(my_stack.pop())
    elif op == 'size':
        print(my_stack.size())
    elif op == 'empty':
        print(my_stack.empty())
    elif op == 'top':
        print(my_stack.top())