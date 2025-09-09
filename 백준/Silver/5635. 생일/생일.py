import sys; input = sys.stdin.readline

n = int(input())
infos = [[name, int(mon), int(day), int(year)] for name, mon, day, year in (input().split() for _ in range(n))]
infos.sort(key=lambda x: (x[3], x[2], x[1]))

print(infos[-1][0])
print(infos[0][0])