def is_good_word(expr):
    stack = []
    for c in expr:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
    if stack:
        return False
    return True

if __name__ == '__main__':
    import sys

    input = sys.stdin.readline
    T = int(input())
    data = [input().strip() for _ in range(T)]

    cnt = 0
    for expr in data:
        if is_good_word(expr) == True:
            cnt += 1
    print(cnt)