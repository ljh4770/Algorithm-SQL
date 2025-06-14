import sys
input = sys.stdin.readline

n = int(input())
names = [tuple(input().rstrip().split(' ')) for _ in range(n)]

dance = set()
dance.add('ChongChong')

for a, b in names:
    if a in dance:
        dance.add(b)
    elif b in dance:
        dance.add(a)
print(len(dance))