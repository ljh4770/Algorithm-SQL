class Deque:
    def __init__(self):
        self.deque = []

    def push_front(self, X):
        self.deque.insert(0, X)

    def push_back(self, X):
        self.deque.append(X)

    def pop_front(self):
        if self.size() == 0:
            return -1
        item = self.deque[0]
        del self.deque[0]
        return item

    def pop_back(self):
        if self.size() == 0:
            return -1
        item = self.deque[-1]
        del self.deque[-1]
        return item

    def size(self):
        return len(self.deque)
    
    def empty(self):
        if self.size() == 0:
            return 1
        return 0

    def front(self):
        if self.size() == 0:
            return -1
        return self.deque[0]

    def back(self):
        if self.size() == 0:
            return -1
        return self.deque[-1]


if __name__ == "__main__":
    import sys

    my_deque = Deque()

    N = int(sys.stdin.readline())
    queries = [sys.stdin.readline().strip() for _ in range(N)]
    for query in queries:
        s = query.split(' ')
        if len(s) > 1:
            op = s[0]
            X = int(s[1])
        else:
            op = s[0]
        
        if op == 'push_front':
            my_deque.push_front(X)
        elif op == 'push_back':
            my_deque.push_back(X)
        else:
            if op == 'pop_front':
                res = my_deque.pop_front()
            elif op == 'pop_back':
                res = my_deque.pop_back()
            elif op == 'size':
                res = my_deque.size()
            elif op == 'empty':
                res = my_deque.empty()
            elif op == 'front':
                res = my_deque.front()
            elif op == 'back':
                res = my_deque.back()
            print(res)