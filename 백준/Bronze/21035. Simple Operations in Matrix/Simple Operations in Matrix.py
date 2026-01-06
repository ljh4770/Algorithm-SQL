import sys; input = sys.stdin.readline

def row_addition(matrix, r, val, n):
    for i in range(n):
        matrix[r][i] += val

def col_addition(matrix, c, val, m):
    for i in range(m):
        matrix[i][c] += val

def evaluation(matrix, n, m):
    sum_ = 0
    min_, max_ = float("inf"), float("-inf")
    for r in range(m):
        for c in range(n):
            v = matrix[r][c]
            sum_ += v
            min_ = min(min_, v)
            max_ = max(max_, v)

    return sum_, min_, max_

if __name__ == "__main__":
    m, n = map(int, input().split())
    matrix = [[*map(int, input().split())] for _ in range(m)]

    q = int(input())
    queries = [tuple(input().rstrip().split()) for _ in range(q)]
    for op, k, val in queries:
        k = int(k) - 1
        val = int(val)
        if op == 'row':
            row_addition(matrix, k, val, n)
        elif op == 'col':
            col_addition(matrix, k, val, m)
    
    print(*evaluation(matrix, n, m))