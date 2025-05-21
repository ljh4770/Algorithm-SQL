import sys
input = sys.stdin.readline

n = int(input())
cords = list(map(int, input().split(' ')))
cords_sorted = sorted(list(set(cords)))
rank = dict()

for r, cord in enumerate(cords_sorted):
    rank[cord] = r
    
for cord in cords:
    print(rank[cord], end=' ')
print()