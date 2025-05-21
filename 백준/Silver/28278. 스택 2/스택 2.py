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

if __name__ == '__main__':
    import sys

    my_stack = IntStack()

    N = int(sys.stdin.readline())
    cmds = [sys.stdin.readline().strip() for _ in range(N)]

    for cmd in cmds:
        cmd = cmd.split(' ')
        op = cmd[0]
        if op == '1':
            my_stack.push(cmd[1])
        elif op == '2':
            print(my_stack.pop())
        elif op == '3':
            print(my_stack.size())
        elif op == '4':
            print(my_stack.empty())
        elif op == '5':
            print(my_stack.top())