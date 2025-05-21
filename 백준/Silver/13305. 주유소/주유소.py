import sys
input = sys.stdin.readline

n = int(input())
road = list(map(int, input().split(' ')))
cost = list(map(int, input().split(' ')))
cost.pop()

answer = 0
cheapest = 10 ** 9 + 1
for c, r in zip(cost, road):
    cheapest = min(cheapest, c)
    answer += cheapest * r
print(answer)