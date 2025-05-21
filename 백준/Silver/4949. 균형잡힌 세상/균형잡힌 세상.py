def isVPS(q):
    stack = []

    for c in q:
        if c == '(':
            stack.append('(')
        elif c == '[':
            stack.append('[')
        elif c == ')':
            if not stack:
                return False
            r = stack.pop()
            if r != '(':
                return False
        elif c == ']':
            if not stack:
                return False
            r = stack.pop()
            if r != '[':
                return False
    
    if stack:
        return False
    
    return True

if __name__ == '__main__':
    import sys

    query = sys.stdin.readline().rstrip()

    while query != '.':
        if isVPS(query) == True:
            print('yes')
        else:
            print('no')
        query = sys.stdin.readline().rstrip()