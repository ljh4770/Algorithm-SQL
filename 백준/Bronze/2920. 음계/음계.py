import sys
input = sys.stdin.readline

data = list(map(int, input().split(' ')))
asc = [i for i in range(1, 9, 1)]
des = [i for i in range(8, 0, -1)]

if data == asc:
    print("ascending")
elif data == des:
    print("descending")
else:
    print("mixed")