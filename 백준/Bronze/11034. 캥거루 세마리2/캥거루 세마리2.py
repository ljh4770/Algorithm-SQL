import sys

for line in sys.stdin:
    a, b, c = map(int, line.split())
    print(max(b - a - 1, c - b - 1))