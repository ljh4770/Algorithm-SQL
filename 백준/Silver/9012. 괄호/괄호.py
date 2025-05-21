import sys

def isVPS(q):
    stack = []

    for c in q:
        if c == '(':
            stack.append('(')
        elif c == ')':
            if not stack:
                return False
            r = stack.pop()
            if r != '(':
                return False
    
    if stack:
        return False
    
    return True


N = int(sys.stdin.readline())

for i in range(N):
    query = sys.stdin.readline()
    if isVPS(query) == True:
        print('YES')
    else:
        print('NO')