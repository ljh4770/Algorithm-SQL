def solve(heights):
    n = heights[0]
    heights = heights[1:]
    stack = []
    prev = 0

    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i if not stack else(i - stack[-1] - 1)
            prev = max(prev, height * width)
        stack.append(i)

    while stack:
        height = heights[stack.pop()]
        width = n if not stack else (n - stack[-1] - 1)
        prev = max(prev, height * width)

    return prev


if __name__ == '__main__':
    import sys

    input = sys.stdin.readline

    while True:
        heights = list(map(int, input().split(' ')))
        if heights[0] == 0:
            break
        print(solve(heights))