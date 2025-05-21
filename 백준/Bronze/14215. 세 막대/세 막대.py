import sys
input = sys.stdin.readline

lengths = [*map(int, input().split(' '))]
lengths.sort()
a, b, c = lengths

if a + b > c:
    print(a + b + c)
else:
    print(2 * (a + b) - 1)