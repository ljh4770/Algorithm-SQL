def solve(expr):
    stack = []
    temp = 1
    res = 0
    prev = ''

    for c in expr:
        if c == '(':
            stack.append(c)
            temp *= 2
        elif c == '[':
            stack.append(c)
            temp *= 3

        elif c == ')':
            if not stack or stack[-1] != '(':
                return 0
            if prev == '(':
                res += temp
            stack.pop()
            temp //= 2

        elif c == ']':
            if not stack or stack[-1] != '[':
                return 0
            if prev == '[':
                res += temp
            stack.pop()
            temp //= 3
        prev = c
    if stack:
        return 0
    
    return res

if __name__ == '__main__':
    import sys

    expr = sys.stdin.readline().strip()
    print(solve(expr))