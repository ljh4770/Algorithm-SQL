def calc(x1, x2, symbol):
    if symbol == '+':
        return x1 + x2
    if symbol == '-':
        return x2 - x1
    if symbol == '*':
        return x1 * x2
    if symbol == '/':
        return x2 / x1  

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    N = int(input())
    expr = input().strip()
    values = [int(input()) for _ in range(N)]

    symbols = ['+', '-', '*', '/']
    operand = dict()
    stack = []

    for i, c in enumerate(range(65, 65 + N, 1)):
        operand[chr(c)] = values[i]

    for c in expr:
        if c in symbols:
            x1 = stack.pop()
            x2 = stack.pop()
            value = calc(x1, x2, c)
            stack.append(value)
        else:
            stack.append(operand[c])

    print(f"{stack[0]:.2f}")