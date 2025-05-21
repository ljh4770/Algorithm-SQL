import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split(' ')))
stack = []
expected = 1

for i, n in enumerate(nums):
    while stack and stack[-1] == expected:
        expected += 1
        stack.pop()
    if n == expected:
        expected += 1
    else:
        stack.append(n)

while stack and stack[-1] == expected:
    expected += 1
    stack.pop()

if stack:
    print('Sad')
else:
    print('Nice')