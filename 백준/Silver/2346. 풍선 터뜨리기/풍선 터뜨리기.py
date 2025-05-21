import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
nums = [*map(int, input().split(' '))]
balloons = deque()
for i, num in enumerate(nums):
    balloons.append((i + 1, num))

answer = []
while balloons:
    idx, num = balloons.popleft()

    if num > 0:
        balloons.rotate(-(num - 1))
    elif num < 0:
        balloons.rotate(-num)

    answer.append(idx)
print(*answer)